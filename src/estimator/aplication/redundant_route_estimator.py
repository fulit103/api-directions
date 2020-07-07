from typing import Optional

from estimator.domain import Route
from estimator.config import Settings

from estimator.aplication import RouteEstimator, RouteNotFoundException, ResponseRouteEstimator
from estimator.infrastructure import RouteEstimatorGraphopperRequest
from estimator.infrastructure import RouteEstimatorGoogleDirectionsRequest

settings = Settings()


def redundant_request_manager(route: Route) -> Optional[ResponseRouteEstimator]:
    try:
        request = RouteEstimatorGraphopperRequest(settings.graphhopper_api)
        route_estimator = RouteEstimator(request)

        response = route_estimator.estimate(route)

        return ResponseRouteEstimator(response.distance, response.time)
    except Exception:
        try:
            request = RouteEstimatorGoogleDirectionsRequest(settings.google_matrix_key)
            route_estimator = RouteEstimator(request)

            response = route_estimator.estimate(route)

            return ResponseRouteEstimator(response.distance, response.time)
        except RouteNotFoundException as rnfe:
            raise RouteNotFoundException
