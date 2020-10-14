from pydantic import BaseSettings


class Settings(BaseSettings):
    graphhopper_api: str = "https://graphhopper.rapigo.co/route"
    auth_token: str = "tokenrapigo"
    google_matrix_key = "a"
    google_geocoder_key = "AIzaSyAknpJmrsqM-z7q7cVvuJtK4mmWW1ZcuOo"
    cors = "http://localhost"
