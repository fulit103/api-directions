from app.boostrap import settings
from estimator.aplication.parallel_geocoder import ParallelGeocoder
from estimator.entrypoints.dto.geocoder_dto import GeocoderResponse, AddressList, PointDTO
from estimator.infrastructure.google_geocoder_repository import GoogleGeocoderRepository
from fastapi import Header, HTTPException, APIRouter
from typing import Optional, List

from estimator.domain import Point

router = APIRouter()


@router.post("/geocoder", response_model=GeocoderResponse)
async def geocoder(addresses: AddressList, x_auth_token: Optional[str] = Header(None)):

    if x_auth_token != settings.auth_token:
        raise HTTPException(status_code=401, detail="Unauthorized user")

    repository = GoogleGeocoderRepository(key=settings.google_geocoder_key)
    use_case = ParallelGeocoder(repository)
    points: List[Point] = await use_case.execute([
       f"{address_dto.address}, {address_dto.city}, {address_dto.country}" for address_dto in addresses.addresses
    ])
    return GeocoderResponse(
        addresses=[
            PointDTO(
                lat=point.latitude,
                lnt=point.longitude
            ) for point in points
        ]
    )