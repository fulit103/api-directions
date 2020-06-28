from estimator.aplication import RouteEstimatorRequest, ResponseRouteEstimator
from estimator.domain import Point
import requests
from pydantic import BaseModel

class PointSerializer(BaseModel, Point):
  pass


class RouteEstimatorGraphopperRequest(RouteEstimatorRequest):

  def __init__(self, url: str):
    self.url = url

  def estimate(self, points: List[Point]): ResponseRouteEstimator
    
    x = requests.post(url, data = myobj)
    
    ResponseRouteEstimator()


