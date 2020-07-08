from typing import List, Optional

from estimator.aplication import RouteEstimator
from estimator.domain import Point, Route
from estimator.domain.adapters import RouteEstimatorRequest, ResponseRouteEstimator


class RouteEstimatorMockRequest(RouteEstimatorRequest):

    def estimate(self, route: Route) -> Optional[ResponseRouteEstimator]:
        return ResponseRouteEstimator(len(route.points) * 2, time=len(route.points))


def test_route_estimator():
    points = [Point(1, 3), Point(1, 3)]

    route = Route(points)
    mock_request = RouteEstimatorMockRequest()
    route_estimate = RouteEstimator(mock_request)
    response = route_estimate.estimate(route)

    assert response.distance == 4
    assert response.time == 2
