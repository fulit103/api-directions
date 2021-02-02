# from estimator.aplication.parallel_geocoder import ParallelGeocoder
# from estimator.aplication.redundant_route_estimator import RedundantRouteEstimator
# from estimator.entrypoints.dto.geocoder_dto import GeocoderResponse, AddressDTO, AddressList, PointDTO
# from estimator.infrastructure import RouteEstimatorGraphhopperRequest, RouteEstimatorGoogleDirectionsRequest, \
#     RouteNotFoundException
# from estimator.infrastructure.google_geocoder_repository import GoogleGeocoderRepository
# from fastapi import FastAPI, Header, HTTPException
# from typing import Optional, List
# from fastapi.middleware.cors import CORSMiddleware
#
# from estimator.config import Settings
# from estimator.entrypoints.dto import EstimateRouteDTO, ResponseRouteDTO
# from estimator.domain import Route, Point, RouteTooSmallException, InvalidLongitudeException, InvalidLatitudeException
#
# settings = Settings()
# app = FastAPI()
#
# origins = settings.cors.split(",")
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=1212)