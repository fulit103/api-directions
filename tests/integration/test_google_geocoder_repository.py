import asyncio
import time

import pytest
from estimator.config import Settings
from estimator.infrastructure.google_geocoder_repository import GoogleGeocoderRepository

settings = Settings()


@pytest.mark.asyncio
async def test_geocode():
    """repository = GoogleGeocoderRepository(key=settings.google_geocoder_key)
    start_time = time.time()
    responses = await asyncio.gather(
        repository.geocode(address="coodelmar 2 etapa casa 2, Pereira, Colombia"),
        repository.geocode(address="colores de la villa, Pereira, Colombia"),
        repository.geocode(address="terminal, Pereira, Colombia"),
    )
    print("--- %s seconds ---" % (time.time() - start_time))
    print([(p.latitude, p.longitude) for p in responses])
    assert responses[0].latitude == 4.7978264
    assert responses[0].longitude == -75.74374209999999

    assert responses[1].latitude == 4.802948199999999
    assert responses[1].longitude == -75.7541267

    assert responses[2].latitude == 4.801614600000001
    assert responses[2].longitude == -75.6932075"""
    assert True
