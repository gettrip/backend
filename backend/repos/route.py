from sqlalchemy.exc import IntegrityError

from backend.db import db_session
from backend.errors import ConflictError, NotFoundError
from backend.models import Place, Route, RoutePoint


class RouteRepo:
    name = 'route'

    def get_all(self) -> list[Route]:
        return Route.query.all()

    def get_by_id(self, uid: int) -> Route:
        route = Route.query.filter(Route.uid == uid).first()
        if not route:
            raise NotFoundError(self.name)

        return route

    def get_by_city(self, city_id: int) -> list[Route]:
        routes = Route.query.filter(Route.city_id == city_id)
        if not routes:
            raise NotFoundError(self.name)

        return routes

    def add(self, name: str, city_id: int) -> Route:
        try:
            route = Route(name=name, city_id=city_id)
            db_session.add(route)
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return route

    def update(self, name: str, uid: int, city_id: int) -> Route:
        route = Route.query.filter(Route.uid == uid).first()
        if not route:
            raise NotFoundError(self.name)

        try:
            route.name = name
            route.city_id = city_id
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return route

    def delete(self, uid: int) -> None:
        points = db_session.query(RoutePoint).filter(Route.uid == uid)
        for point in points:
            db_session.delete(point)
        route = Route.query.filter(Route.uid == uid).first()
        db_session.delete(route)
        db_session.commit()

    def add_point(
        self, route_id: int, position: int, place_id: int, distance: int,
    ) -> RoutePoint:
        try:
            routepoint = RoutePoint(
                position=position,
                place_id=place_id,
                route_id=route_id,
                distance=distance,
            )
            db_session.add(routepoint)
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return routepoint

    def get_points(self, route_id: int) -> list[Place]:
        return db_session.query(
            Place,
        ).join(
            RoutePoint.place,
            RoutePoint.route,
        ).filter(Route.uid == route_id)

    def delete_point(self, route_id: int, place_id: int) -> None:
        point = RoutePoint.query.filter(
            RoutePoint.route_id == route_id,
            RoutePoint.place_id == place_id,
        ).first()
        db_session.delete(point)
        db_session.commit()
