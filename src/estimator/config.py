from pydantic import BaseSettings


class Settings(BaseSettings):
    graphhopper_api: str = "https://graphhopper.rapigo.co/route"
    auth_token: str = "tokenrapigo"
    google_matrix_key = "a"
    cors = "http://localhost"
