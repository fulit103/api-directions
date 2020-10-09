from typing import Optional

from estimator.domain import Point
from estimator.domain.adapters.geocoder_repository import GeocoderRepository


class GoogleGeocoderRepository(GeocoderRepository):

    def __init__(self, key: str):
        self.client = googlemaps.Client(key=key)


    async def geocode(self, address: str) -> Optional[Point]:
        pass