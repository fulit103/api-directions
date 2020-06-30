from fastapi import FastAPI, Header, status, HTTPException
from fastapi.responses import JSONResponse
from typing import List, Optional

from estimator.config import Settings
from estimator.entrypoints.dto import EstimateRouteDTO, ResponseRouteDTO
from estimator.domain import Route, Point
from estimator.aplication import RouteEstimator
from estimator.infrastructure import RouteEstimatorGraphopperRequest

settings = Settings()
app = FastAPI()

@app.post("/route", response_model=ResponseRouteDTO)
def route(route_dto:EstimateRouteDTO, x_auth_token: Optional[str] = Header(None) ):
  
  if x_auth_token != settings.auth_token:
    raise HTTPException(status_code=401, detail="Unauthorized user")

  try:
    points = [ Point(longitude=point.lon, latitude=point.lat) for point in route_dto.points]
    route = Route(points)

    request = RouteEstimatorGraphopperRequest(settings.graphhopper_api)
    route_estimator = RouteEstimator(request)

    response = route_estimator.estimate(route)
    data = {"distance": response.distance, "time": response.time}
    
    return ResponseRouteDTO(**data)
  except:
    raise HTTPException(status_code=422, detail="Error de dominio")
  

  
  
