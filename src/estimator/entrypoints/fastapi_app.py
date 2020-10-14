from estimator.aplication.parallel_geocoder import ParallelGeocoder
from estimator.aplication.redundant_route_estimator import RedundantRouteEstimator
from estimator.entrypoints.dto.geocoder_dto import GeocoderResponse, AddressDTO, AddressList, PointDTO
from estimator.infrastructure import RouteEstimatorGraphhopperRequest, RouteEstimatorGoogleDirectionsRequest, \
    RouteNotFoundException
from estimator.infrastructure.google_geocoder_repository import GoogleGeocoderRepository
from fastapi import FastAPI, Header, HTTPException
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware

from estimator.config import Settings
from estimator.entrypoints.dto import EstimateRouteDTO, ResponseRouteDTO
from estimator.domain import Route, Point, RouteTooSmallException, InvalidLongitudeException, InvalidLatitudeException

settings = Settings()
app = FastAPI()

origins = settings.cors.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/geocoder", response_model=GeocoderResponse)
async def geocoder(addresses: AddressList, x_auth_token: Optional[str] = Header(None)):

    if x_auth_token != settings.auth_token:
        raise HTTPException(status_code=401, detail="Unauthorized user")

    repository = GoogleGeocoderRepository(key=settings.google_geocoder_key)
    use_case = ParallelGeocoder(repository)
    points: List[Point] = await use_case.execute([
       f"{address_dto.address}, {address_dto.city}, {address_dto.country}" for address_dto in addresses.addresses
    ])
    return GeocoderResponse(
        addresses=[
            PointDTO(
                lat=point.latitude,
                lnt=point.longitude
            ) for point in points
        ]
    )


@app.post("/route", response_model=ResponseRouteDTO)
def route(route_dto: EstimateRouteDTO, x_auth_token: Optional[str] = Header(None)):

    if x_auth_token != settings.auth_token:
        raise HTTPException(status_code=401, detail="Unauthorized user")

    try:        
        points = [Point(longitude=point.lon, latitude=point.lat) for point in route_dto.points]
        route = Route(points)        
        request_graphhopper = RouteEstimatorGraphhopperRequest(settings.graphhopper_api)
        request_google_directions = RouteEstimatorGoogleDirectionsRequest(settings.google_matrix_key)
        route_estimator = RedundantRouteEstimator(
            request1=request_graphhopper,
            request2=request_google_directions
        )
        response = route_estimator.estimate(route)
        data = {"distance": response.distance, "time": response.time}
        return ResponseRouteDTO(**data)
    except InvalidLongitudeException as e:
        raise HTTPException(status_code=422, detail=e)
    except InvalidLatitudeException as e:
        raise HTTPException(status_code=422, detail=e)
    except RouteTooSmallException as e:
        raise HTTPException(status_code=422, detail=e)
    except RouteNotFoundException as e:
        raise HTTPException(status_code=400, detail=e)
    except Exception as e:
        raise HTTPException(status_code=400, detail=e)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=1212)