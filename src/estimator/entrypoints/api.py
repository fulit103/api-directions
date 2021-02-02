from estimator.entrypoints.endpoints import geocoder, optimize, route
from fastapi import APIRouter


api_router = APIRouter()

api_router.include_router(geocoder.router)
api_router.include_router(optimize.router)
api_router.include_router(route.router)
