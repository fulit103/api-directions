import pytest
from estimator.domain import Point, Route
from estimator.config import Settings
from estimator.infrastructure import serialize_points, RouteEstimatorGraphhopperRequest, PointOutOfBoundsException, \
    transform_distance, RouteNotFoundException
from .utils import get_valid_route

settings = Settings()


def test_serialize_four_points():
    points = [
        Point(latitude=2.1, longitude=1.1),
        Point(latitude=3.1, longitude=2.1),
        Point(latitude=4.1, longitude=3.1),
        Point(latitude=5.1, longitude=4.1)
    ]

    data = serialize_points(points)

    assert data[0][0] == 1.1
    assert data[0][1] == 2.1

    assert data[1][0] == 2.1
    assert data[1][1] == 3.1

    assert data[2][0] == 3.1
    assert data[2][1] == 4.1

    assert data[3][0] == 4.1
    assert data[3][1] == 5.1

    assert len(data) == 4


def test_serialize_empty_points():
    points = []
    data = serialize_points(points)
    assert len(data) == 0


def test_request_graphopper():
    route = get_valid_route()

    request = RouteEstimatorGraphhopperRequest(settings.graphhopper_api)
    response = request.estimate(route)

    assert response.distance > 0
    assert response.time > 0


def test_request_graphopper_optimize():
    points = [
        Point(-75.71378409,4.80899459),
        Point(-75.71451885,4.81067301),
        Point(-75.71212962,4.80898457),
        Point(-75.7114867,4.807989399999999)
    ]
    route = Route(points)

    request = RouteEstimatorGraphhopperRequest("https://graphhopper.com/api/1/route?key=9cf6fbe5-2ab9-4c19-bdce-3ce707da3d92")
    response = request.estimate(route, optimize=True)

    assert response.distance > 0
    assert response.time > 0

    assert [0, 2, 1, 3] == response.points_order


def test_request_graphhopper_point_out_of_bounds():
    points = [
        Point(-74.072090, 4.710989),
        Point(-74.090984, 20)
    ]
    route = Route(points)

    with pytest.raises(PointOutOfBoundsException):
        request = RouteEstimatorGraphhopperRequest(settings.graphhopper_api)
        request.estimate(route)


def test_request_graphhopper_distance_0():
    points = [
        Point(-75.566564, 6.246225),
        Point(-75.566564, 6.246225)
    ]
    route = Route(points)

    with pytest.raises(RouteNotFoundException):
        request = RouteEstimatorGraphhopperRequest(settings.graphhopper_api)
        request.estimate(route)


def test_transform_distance():
    assert transform_distance(1000) == 1000
    assert transform_distance(1001) == 2000
    assert transform_distance(1501) == 3000

    assert transform_distance(3000) == 3000
    assert transform_distance(3001) == 4000
    assert transform_distance(3501) == 5000

    assert transform_distance(9000) == 9000
    assert transform_distance(9001) == 10000
    assert transform_distance(9501) == 11000
