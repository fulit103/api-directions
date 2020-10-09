import abc
from typing import Optional

from estimator.domain import Point


class GeocoderRepository(abc.ABC):

    @abc.abstractmethod
    async def geocode(self, address: str) -> Optional[Point]: pass
