import abc
from typing import Optional, List

from estimator.domain import Route


class RouteNotFoundException(Exception):
    def __init__(self):
        self.message = f"No valid route found"
        super().__init__(self.message)


class ResponseRouteEstimator:
    distance: int
    time: int
    points_order: List[int]

    def __init__(self, distance: int, time: int = None, points_order: List[int] = None):
        self.distance = distance
        self.time = time
        self.points_order = points_order


class RouteEstimatorRequest(abc.ABC):

    @abc.abstractmethod
    def estimate(self, route: Route, optimize: bool) -> Optional[ResponseRouteEstimator]:
        raise NotImplementedError
