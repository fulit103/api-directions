import requests
from typing import List, Optional
import math

from estimator.domain import Point, Route
from estimator.domain.adapters import RouteEstimatorRequest, ResponseRouteEstimator, RouteNotFoundException


class PointOutOfBoundsException(Exception):
    pass


def serialize_points(points: List[Point]):
    return [[point.longitude, point.latitude] for point in points]


def transform_distance(distance: float) -> int:
    decimals = distance - int(distance / 1000.0) * 1000

    if 0 < decimals < 500:
        return math.ceil(distance / 1000.0) * 1000

    if decimals > 500:
        return math.ceil(distance / 1000.0) * 1000 + 1000

    return math.ceil(distance / 1000.0) * 1000


class RouteEstimatorGraphhopperRequest(RouteEstimatorRequest):

    def __init__(self, url: str):
        self.url = url

    def estimate(self, route: Route) -> Optional[ResponseRouteEstimator]:
        response = requests.post(self.url, json={
            "points": serialize_points(route.points),
            "instructions": False,
            "calc_points": False,
            "elevation": True,
            "vehicle": "car",
            "avoid": "secondary"
        }, timeout=2)
        response_json = response.json()
        print(response_json)
        status_code = response.status_code
        if status_code == 400:
            if response_json["hints"][0]["details"] == "com.graphhopper.util.exceptions.PointOutOfBoundsException":
                raise PointOutOfBoundsException(response_json["message"])

        if status_code == 200:
            distance = transform_distance(response_json["paths"][0]["distance"])
            time = response_json["paths"][0]["time"]

            if distance == 0:
                raise RouteNotFoundException()

            return ResponseRouteEstimator(int(distance/1000.0), time=int(time))
        else:
            return None
