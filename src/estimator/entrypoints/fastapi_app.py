from estimator.aplication.redundant_route_estimator import RedundantRouteEstimator
from estimator.infrastructure import RouteEstimatorGraphhopperRequest, RouteEstimatorGoogleDirectionsRequest, \
    RouteNotFoundException
from fastapi import FastAPI, Header, HTTPException
from typing import Optional

from estimator.config import Settings
from estimator.entrypoints.dto import EstimateRouteDTO, ResponseRouteDTO
from estimator.domain import Route, Point, RouteTooSmallException, InvalidLongitudeException, InvalidLatitudeException

settings = Settings()
app = FastAPI()


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
