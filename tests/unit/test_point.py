from estimator.domain import Point, InvalidLatitudeException, InvalidLongitudeException
import pytest

def test_invalid_point():

  with pytest.raises(Exception):
    point = Point()

  with pytest.raises(Exception):
    point = Point(longitude=2)

  with pytest.raises(Exception):
    point = Point(latitude=2)

  with pytest.raises(Exception):
    point = Point(longitude=2, latitude=None)

  with pytest.raises(Exception):
    point = Point(longitude=None, latitude=None)

  with pytest.raises(Exception):
    point = Point(latitude="2")

  with pytest.raises(Exception):
    point = Point(latitude="2", longitude="33")

  with pytest.raises(InvalidLatitudeException):
    point = Point(latitude=91, longitude=33)
  
  with pytest.raises(InvalidLongitudeException):
    point = Point(latitude=90, longitude=182)

  Point(latitude=90, longitude=180)
  Point(latitude=-90, longitude=-180)