from estimator.aplication.redundant_route_estimator import RedundantRouteEstimator
from typing import List
from app.boostrap import settings
from fastapi import HTTPException, APIRouter
from pydantic.main import BaseModel
from estimator.entrypoints.dto import EstimateRouteDTO, ResponseRouteDTO
from estimator.domain import Point, Route, RouteTooSmallException, InvalidLongitudeException, InvalidLatitudeException
from estimator.infrastructure import RouteEstimatorGraphhopperRequest, RouteEstimatorGoogleDirectionsRequest, RouteNotFoundException

router = APIRouter()


class PointDTO(BaseModel):
    lat: float
    lon: float
    key: str


class RouteDTO(BaseModel):
    points: List[PointDTO]


class ResponseRouteOptimized(BaseModel):
    keys: List[str]


@router.post("/optimize")
def optimize(route_optimizer: EstimateRouteDTO):

    try:
        points = [Point(longitude=point.lon, latitude=point.lat)
                  for point in route_optimizer.points]
        route = Route(points)
        request_graphhopper = RouteEstimatorGraphhopperRequest(
            'https://graphhopper.com/api/1/route?key=9cf6fbe5-2ab9-4c19-bdce-3ce707da3d92')
        r = request_graphhopper.estimate(route, optimize=True)
        return {"points": r.points_order}
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
