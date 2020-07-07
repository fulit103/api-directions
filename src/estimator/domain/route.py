from typing import Optional, List, Set
from .point import Point

class RouteTooSmallException(Exception):
  def __init__(self, points ):
    self.message = f"Routes has minimun 2 points, {len(points)}"
    super().__init__(self.message)

class Route:
  points: List[Point]

  def __init__(self, points: List[Point]):
    self.guard(points)
    self.points = points

  def guard(self, points):
    if points==None or len(points)<=1:
      raise RouteTooSmallException(points)
  
  """
    return origin point
  """
  def origin(self):
    return self.points[0]

  """
    return array with destinations points
  """
  def destinations(self):
    return self.points[1:]

  """
    return destination point
  """
  def destination(self):
    return self.points[len(self.points)-1]

  """
    return array waypoints
  """
  def waypoints(self):
    size = len(self.points)
    print(size)
    if size>=3:
      return self.points[1:size-1]
    return None
