import googlemaps
from typing import Optional

from estimator.domain import Route
from estimator.aplication import RouteEstimatorRequest, ResponseRouteEstimator

from .google import point_to_json


class RouteEstimatorGoogleMatrixRequest(RouteEstimatorRequest):

    def __init__(self, key: str):
        self.client = googlemaps.Client(key=key)

    def estimate(self, route: Route) -> Optional[ResponseRouteEstimator]:
        origins = [
            point_to_json(route.origin())
        ]

        destinations = [point_to_json(p) for p in route.destinations()]

        matrix = self.client.distance_matrix(origins, destinations)

        return ResponseRouteEstimator(1, 1)
