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





def test_route_origin():
  points = [
    Point(99,77),
    Point(33,23),
    Point(44,22)
  ]
  route = Route(points)

  assert route.origin()==points[0]



def test_route_destination():
  points = [
    Point(99,77),
    Point(33,23),
    Point(44,22)
  ]
  route = Route(points)

  assert route.destination()==points[2]

def test_route_weypoints():
  points = [
    Point(99,77),
    Point(33,23),
    Point(44,22)
  ]
  route = Route(points)

  assert len(route.waypoints())==1

  points = [
    Point(99,77),
    Point(45,23),
    Point(56,17),
    Point(44,22)
  ]
  route = Route(points)  

  assert len(route.waypoints())==2