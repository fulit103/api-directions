from pydantic import BaseModel


class AddressDTO(BaseModel):
    address: str
    city: str


class GeocoderResponse(BaseModel):
    lat: float = None
    lon: float = None
