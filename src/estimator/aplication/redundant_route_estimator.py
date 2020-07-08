from typing import Optional

from estimator.config import Settings
from estimator.domain.adapters import RouteEstimatorRequest, ResponseRouteEstimator, RouteNotFoundException

settings = Settings()


class RedundantRouteEstimator:

    def __init__(self, request1: RouteEstimatorRequest, request2: RouteEstimatorRequest):
        self.request1 = request1
        self.request2 = request2

    def estimate(self, route) -> Optional[ResponseRouteEstimator]:
        try:
            response = self.request1.estimate(route)
            return ResponseRouteEstimator(response.distance, response.time)
        except Exception:
            response = self.request2.estimate(route)
            return ResponseRouteEstimator(response.distance, response.time)

