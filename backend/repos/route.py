from sqlalchemy.exc import IntegrityError

from backend.db import db_session
from backend.errors import ConflictError, NotFoundError
from backend.models import Route, RoutePlace


class RouteRepo:
    name = 'route'

    def get_all(self) -> list[Route]:
        return Route.query.all()

    def get_by_id(self, uid: int) -> Route:
        route = Route.query.filter(Route.uid == uid).first()
        if not route:
            raise NotFoundError(self.name)

        return route

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
        route = Route.query.filter(Route.uid == uid).first()
        db_session.delete(route)
        db_session.commit()

    def get_position(self, route_id):
        query = RoutePlace.query.filter(RoutePlace.route_id == route_id)
        route = query.order_by(RoutePlace.position.desc()).first()
        if not route:
            return 1

        return route.position + 1

    def add_routeplace(
        self, route_id: int, position: int, place_id: int, distance: int,
    ) -> RoutePlace:
        try:
            routeplace = RoutePlace(
                position=position,
                place_id=place_id,
                route_id=route_id,
                distance=distance,
            )
            db_session.add(routeplace)
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name)

        return routeplace

    def get_all_routplaces(self) -> list[RoutePlace]:
        return RoutePlace.query.all()

    def delete_routeplace(self, route_id: int, place_id: int) -> None:
        routeplace = RoutePlace.query.filter(
            RoutePlace.route_id == route_id,
            RoutePlace.place_id == place_id,
        ).first()
        db_session.delete(routeplace)
        db_session.commit()
