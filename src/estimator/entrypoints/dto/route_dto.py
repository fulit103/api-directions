from pydantic import BaseModel
from typing import Optional, List


class PointDTO(BaseModel):
    lat: float
    lon: float


class EstimateRouteDTO(BaseModel):
    points: List[PointDTO]
    country: str = "colombia"


class ResponseRouteDTO(BaseModel):
    distance: Optional[float] = None
    time: Optional[float] = None
