import abc
from typing import Optional

from estimator.domain import Route


class RouteNotFoundException(Exception):
    def __init__(self):
        self.message = f"No valid route found"
        super().__init__(self.message)


class ResponseRouteEstimator:
    distance: int
    time: int

    def __init__(self, distance: int, time: int = None):
        self.distance = distance
        self.time = time


class RouteEstimatorRequest(abc.ABC):

    @abc.abstractmethod
    def estimate(self, route: Route) -> Optional[ResponseRouteEstimator]:
        raise NotImplementedError