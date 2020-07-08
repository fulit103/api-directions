from typing import Optional

import pytest
from estimator.aplication import RedundantRouteEstimator
from estimator.domain import Route, Point
from estimator.domain.adapters import RouteEstimatorRequest, ResponseRouteEstimator


class RouteEstimatorFailMockRequest(RouteEstimatorRequest):

    def estimate(self, route: Route) -> Optional[ResponseRouteEstimator]:
        raise Exception("mock error")


class RouteEstimatorMockRequest(RouteEstimatorRequest):

    def estimate(self, route: Route) -> Optional[ResponseRouteEstimator]:
        return ResponseRouteEstimator(len(route.points) * 2, time=len(route.points))


def test_redundant_route_estimator():
    points = [Point(1, 3), Point(1, 3)]
    route = Route(points)

    request1 = RouteEstimatorFailMockRequest()
    request2 = RouteEstimatorMockRequest()

    redundant_route_estimator = RedundantRouteEstimator(request1=request1, request2=request2)
    response = redundant_route_estimator.estimate(route)
    assert response.distance == 4
    assert response.time == 2

    redundant_route_estimator = RedundantRouteEstimator(request1=request2, request2=request1)
    response = redundant_route_estimator.estimate(route)
    assert response.distance == 4
    assert response.time == 2

    with pytest.raises(Exception):
        redundant_route_estimator = RedundantRouteEstimator(request1=request1, request2=request1)
        redundant_route_estimator.estimate(route)
