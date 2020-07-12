from estimator.aplication.redundant_route_estimator import RedundantRouteEstimator
from estimator.infrastructure import RouteEstimatorGraphhopperRequest, RouteEstimatorGoogleDirectionsRequest, \
    RouteNotFoundException
from fastapi import FastAPI, Header, HTTPException
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

from estimator.config import Settings
from estimator.entrypoints.dto import EstimateRouteDTO, ResponseRouteDTO
from estimator.domain import Route, Point, RouteTooSmallException, InvalidLongitudeException, InvalidLatitudeException

settings = Settings()
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/route", response_model=ResponseRouteDTO)
def route(route_dto: EstimateRouteDTO, x_auth_token: Optional[str] = Header(None)):

    if x_auth_token != settings.auth_token:
        raise HTTPException(status_code=401, detail="Unauthorized user")

    try:
        print(route_dto)
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
        print(e)
        raise HTTPException(status_code=400, detail=e)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=1212)