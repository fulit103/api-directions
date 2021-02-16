from fastapi.testclient import TestClient
from estimator.config import Settings

from app.fastapi import app

client = TestClient(app)


def test_route_api_value_error():
    response = client.post("/route")
    assert response.status_code == 422

    data = {}
    response = client.post("/route", json=data)
    assert response.status_code == 422

    data = {
        "points": [
            {"lat": 343}
        ]
    }
    response = client.post("/route", json=data)
    assert response.status_code == 422


def test_route_api():
    settings = Settings()
    token = settings.auth_token
    headers = {'x-auth-token': token}
    data = {
        "points": [
            {"lat": 4.710989, "lon": -74.072090},
            {"lat": 4.638023, "lon": -74.090984},
            {"lat": 4.732464, "lon": -74.130836}
        ],
        "country": "colombia"
    }
    response = client.post("/route", json=data, headers=headers)
    assert response.status_code == 200


def test_route_api_unauthorized():
    data = {"points": []}
    headers = {'x-auth-token': "invalid"}
    response = client.post("/route", json=data, headers=headers)
    assert response.status_code == 401
