from estimator.domain import Point


def point_to_json(p: Point):
    return {
        "lat": p.latitude,
        "lng": p.longitude
    }
