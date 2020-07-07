from estimator.domain import Route, Point
from estimator.config import Settings

from estimator.infrastructure import RouteEstimatorGoogleDirectionsRequest

from .utils import get_valid_route

settings = Settings()

def test_request_google_matrix():
  route = get_valid_route()
  request = RouteEstimatorGoogleDirectionsRequest(key=settings.google_matrix_key)
  response = request.estimate(route)  

  print(f"distance: {response.distance} , duration: {response.time}")

  assert response.distance>0
  assert response.time>0