from pydantic import BaseSettings


class Settings(BaseSettings):
    graphhopper_api: str = "https://graphhopper.rapigo.co/route"
    auth_token: str = "tokenrapigo"
    google_matrix_key = "a"
    google_geocoder_key = "a"
    cors = "http://localhost"
    graphhopper_api_optimizate = "https://graphhopper.com/api/1/route?key=9cf6fbe5-2ab9-4c19-bdce-3ce707da3d92"
