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

    def estimate(self, route: Route, optimize: bool = False) -> Optional[ResponseRouteEstimator]:
        parameters = {
            "points": serialize_points(route.points),
            "instructions": False,
            "calc_points": False,
            "elevation": True,
            "vehicle": "car",
            "avoid": "secondary"
        }

        if optimize is True:
            parameters["optimize"] = "true"
            # parameters["avoid"] = "secondary"
            # parameters["ch.disable"] = True
            # parameters["Weighting"] = "short_fastes"

        response = requests.post(self.url, json=parameters, timeout=2)
        response_json = response.json()
        status_code = response.status_code
        if status_code == 400:
            if response_json["hints"][0]["details"] == "com.graphhopper.util.exceptions.PointOutOfBoundsException":
                raise PointOutOfBoundsException(response_json["message"])

        if status_code == 200:
            distance = transform_distance(response_json["paths"][0]["distance"])
            time = response_json["paths"][0]["time"]
            points_order = None

            if optimize is True:
                points_order = response_json["paths"][0]["points_order"]

            if distance == 0:
                raise RouteNotFoundException()

            return ResponseRouteEstimator(int(distance/1000.0), time=int(time), points_order=points_order)
        else:
            return None
