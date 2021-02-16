from pydantic import BaseModel
from typing import List


class ResponseRouteOptimize(BaseModel):
    points: List[int]
