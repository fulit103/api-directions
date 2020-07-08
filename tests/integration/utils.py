from estimator.domain import Route, Point


def get_valid_route():
    points = [
        Point(-74.072090, 4.710989),
        Point(-74.090984, 4.638023),
        Point(-74.08525507, 4.73773701),
        Point(-74.06204284, 4.75025352)
    ]
    route = Route(points)
    return route
