from typing import Optional

from aiogmaps import Client
from estimator.domain import Point
from estimator.domain.adapters.geocoder_repository import GeocoderRepository


class GoogleGeocoderRepository(GeocoderRepository):

    def __init__(self, key: str):
        self._client: Client = Client(key)

    async def geocode(self, address: str) -> Optional[Point]:
        response = await self._client.geocode(
            address=address
        )

        if len(response) == 0 or "geometry" not in response[0]:
            return None

        return Point(
            latitude=response[0]["geometry"]["location"]["lat"],
            longitude=response[0]["geometry"]["location"]["lng"]
        )
