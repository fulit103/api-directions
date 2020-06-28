from typing import Optional, List, Set
from .point import Point

class Route:
  points: List[Point]

  def __init__(self, points: List[Point]):
    self.points = points