import requests
from typing import List, Optional
from pydantic import BaseModel

from estimator.domain import Point, Route
from estimator.aplication import RouteEstimatorRequest, ResponseRouteEstimator

class PointOutOfBoundsException(Exception):
  pass

def serialize_points(points: List[Point]):
  return [[point.longitude, point.latitude] for point in points ]

class RouteEstimatorGraphopperRequest(RouteEstimatorRequest):

  def __init__(self, url: str):
    self.url = url

  def estimate(self, route: Route) -> Optional[ResponseRouteEstimator]:    
    response = requests.post(self.url, json = {
      "points": serialize_points(route.points),
      "instructions": False,
	    "calc_points": False
    }, timeout=2)    
    response_json = response.json()    
    status_code = response.status_code
    if status_code==400:
      if response_json["hints"][0]["details"] == "com.graphhopper.util.exceptions.PointOutOfBoundsException":
        raise PointOutOfBoundsException(response_json["message"])

    if status_code==200:
      distance = response_json["paths"][0]["distance"]
      time = response_json["paths"][0]["time"]
      return ResponseRouteEstimator(int(distance), time=int(time))
    else:
      return None


