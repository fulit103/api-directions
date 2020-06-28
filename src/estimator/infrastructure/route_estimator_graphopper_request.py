import requests
from typing import List
from pydantic import BaseModel

from estimator.domain import Point
from estimator.aplication import RouteEstimatorRequest, ResponseRouteEstimator

class PointSerializer(BaseModel, Point):
  pass


class RouteEstimatorGraphopperRequest(RouteEstimatorRequest):

  def __init__(self, url: str):
    self.url = url

  def estimate(self, points: List[Point]) -> ResponseRouteEstimator:
    x = requests.post(url, data = myobj)    
    return ResponseRouteEstimator()


