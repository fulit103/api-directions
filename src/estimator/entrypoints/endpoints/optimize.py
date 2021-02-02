from typing import List

from fastapi import APIRouter
from pydantic.main import BaseModel

router = APIRouter()


class PointDTO(BaseModel):
    lat: float
    lon: float
    key: str


class RouteDTO(BaseModel):
    points: List[PointDTO]


class ResponseRouteOptimized(BaseModel):
    keys: List[str]


@router.post("/optimize", response_model=ResponseRouteOptimized)
async def optimize(dto: RouteDTO):
    response = {
        "keys": [1, 2, 3]
    }
    return ResponseRouteOptimized(**response)
