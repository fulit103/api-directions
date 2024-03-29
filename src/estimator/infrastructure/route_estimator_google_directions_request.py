import googlemaps
from typing import Optional

from estimator.domain import Route
from estimator.domain.adapters import RouteEstimatorRequest, ResponseRouteEstimator

from .google import point_to_json


class RouteEstimatorGoogleDirectionsRequest(RouteEstimatorRequest):

    def __init__(self, key: str, transform_distance: bool):
        self.client = googlemaps.Client(key=key)
        self.transform_distance = transform_distance

    def estimate(self, route: Route) -> Optional[ResponseRouteEstimator]:
        origin = point_to_json(route.origin())
        destination = point_to_json(route.destination())
        waypoints = [point_to_json(p) for p in route.waypoints()] if route.waypoints() != None else None

        matrix = self.client.directions(origin, destination, waypoints=waypoints)

        if len(matrix) == 0:
            return None

        legs = matrix[0]["legs"]

        distance = 0
        duration = 0
        for leg in legs:
            distance = distance + leg["distance"]["value"]
            duration = distance + leg["duration"]["value"]

        if self.transform_distance:
            distance = int(distance/1000)
        else:
            distance = float("{:.1f}".format(distance/1000))

        if distance == 0:
            distance = 1

        return ResponseRouteEstimator(distance, duration)
