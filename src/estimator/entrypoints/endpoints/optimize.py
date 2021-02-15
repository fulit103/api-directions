from estimator.aplication.redundant_route_estimator import RedundantRouteEstimator
from typing import List, Optional
from app.boostrap import settings
from fastapi import HTTPException, APIRouter, Header
from pydantic.main import BaseModel
from estimator.entrypoints.dto import EstimateRouteDTO, ResponseRouteOptimize
from estimator.domain import Point, Route, RouteTooSmallException, InvalidLongitudeException, InvalidLatitudeException
from estimator.infrastructure import RouteEstimatorGraphhopperRequest, RouteEstimatorGoogleDirectionsRequest, RouteNotFoundException

router = APIRouter()


@router.post("/optimize", response_model=ResponseRouteOptimize)
def optimize(route_optimizer: EstimateRouteDTO, x_auth_token: Optional[str] = Header(None)):

    if x_auth_token != settings.auth_token:
        raise HTTPException(status_code=401, detail="Unauthorized user")

    try:
        points = [Point(longitude=point.lon, latitude=point.lat)
                  for point in route_optimizer.points]
        route = Route(points)
        request_graphhopper = RouteEstimatorGraphhopperRequest(
            settings.graphhopper_api_optimizate)
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
