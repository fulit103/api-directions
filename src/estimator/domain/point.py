class InvalidLongitudeException(Exception):
    def __init__(self, longitude):
        self.message = f"Longitude can't be null and is a number between (180, -180) , longitude={longitude}"
        super().__init__(self.message)


class InvalidLatitudeException(Exception):
    def __init__(self, latitude):
        self.message = f"Latitude can't be null and is a number between (90, -90) , latitude={latitude}"
        super().__init__(self.message)


class Point:
    longitude: float
    latitude: float

    def __init__(self, longitude: float, latitude: float):
        self.guard_longitude(longitude)
        self.longitude = longitude
        self.guard_latitude(latitude)
        self.latitude = latitude

    def guard_longitude(self, longitude: float):
        if longitude == None or longitude > 180 or longitude < -180:
            raise InvalidLongitudeException(longitude)

    def guard_latitude(self, latitude: float):
        if latitude == None or latitude > 90 or latitude < -90:
            raise InvalidLatitudeException(latitude)
