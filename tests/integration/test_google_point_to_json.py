from estimator.domain import Point
from estimator.infrastructure.google import point_to_json


def test_point_to_json():
    point = Point(longitude=1, latitude=2)

    json = point_to_json(point)

    assert json["lat"] == point.latitude
    assert json["lng"] == point.longitude
