import asyncio
from typing import List

from estimator.domain import Point
from estimator.domain.adapters.geocoder_repository import GeocoderRepository


class ParallelGeocoder:

    def __init__(self, repository: GeocoderRepository):
        self._geocoder_repository = repository

    async def execute(self, addresses: List[str]) -> List[Point]:
        points = await asyncio.gather(
            *[self._geocoder_repository.geocode(address=address) for address in addresses]
        )
        return points
