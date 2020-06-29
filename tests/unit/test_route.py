import pytest
from estimator.domain import Route, Point, RouteTooSmallException

def test_invalid_route():
  points = []
  with pytest.raises(RouteTooSmallException):
    Route(points)

  points = [
    Point(99,77)
  ]
  with pytest.raises(RouteTooSmallException):
    Route(points)

  points = [
    Point(99,77),
    Point(33,23)
  ]
  route = Route(points)

  points = [
    Point(99,77),
    Point(33,23),
    Point(44,22)
  ]
  route = Route(points)
