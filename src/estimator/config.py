from pydantic import BaseSettings


class Settings(BaseSettings):
    graphhopper_api: str = "https://graphhopper.rapigo.co/route"
    auth_token: str = "aAbdeerergssdgRCEdserdf"
