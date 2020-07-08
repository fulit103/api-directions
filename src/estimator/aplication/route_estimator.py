import abc
from typing import List, Optional
from estimator.domain import Point, Route
from estimator.domain.adapters import RouteEstimatorRequest, ResponseRouteEstimator

"""
Use case estimate time and distance of a route
"""


class RouteEstimator:

    def __init__(self, adapter: RouteEstimatorRequest):
        self.adapter = adapter

    def estimate(self, route: Route) -> Optional[ResponseRouteEstimator]:
        return self.adapter.estimate(route)
