import abc
from typing import List
from estimator.domain import Point

class ResponseRouteEstimator:
  distance: int
  time: int

class RouteEstimatorRequest(abc.ABC):

  @abc.abstractmethod
  def estimate(self, points: List[Point]) -> ResponseRouteEstimator:
    raise NotImplementedError

"""
Use case estimate time and distance of a route
"""
class RouteEstimator:

  def __init__(self, adapter: RouteEstimatorRequest):
    self.adapter = adapter

  def estimate(self, points: List[Point]) -> ResponseRouteEstimator:
    return self.adapter.estimate(points)