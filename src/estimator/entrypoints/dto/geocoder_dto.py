from typing import List

from pydantic import BaseModel


class AddressDTO(BaseModel):
    address: str
    city: str
    country: str


class AddressList(BaseModel):
    addresses: List[AddressDTO]


class PointDTO(BaseModel):
    lat: float = None
    lnt: float = None


class GeocoderResponse(BaseModel):
    addresses: List[PointDTO]
