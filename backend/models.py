from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint, String, UniqueConstraint
from sqlalchemy.orm import RelationshipProperty, relationship

from backend.db import Base, engine


class City(Base):
    __tablename__ = 'cities'

    uid = Column(Integer, primary_key=True)
    name = Column(String(), unique=True, nullable=False)

    def __str__(self) -> str:
        return 'City {uid}, {name}'.format(
            uid=self.uid,
            name=self.name,
        )


class User(Base):
    __tablename__ = 'users'

    uid = Column(Integer, primary_key=True)
    username = Column(String(), unique=True)

    def __str__(self) -> str:
        return 'User {uid}, {username}'.format(
            uid=self.uid,
            username=self.username,
        )


class Place(Base):
    __tablename__ = 'places'

    uid = Column(Integer, primary_key=True)
    city_id = Column(Integer, ForeignKey(City.uid), nullable=False)
    name = Column(String(), unique=True, nullable=False)
    routes: RelationshipProperty = relationship('RoutePoint')

    def __str__(self) -> str:
        return 'Place {uid}, {name}'.format(
            uid=self.uid,
            name=self.name,
        )


class Route(Base):
    __tablename__ = 'routes'

    uid = Column(Integer, primary_key=True)
    name = Column(String(), unique=True, nullable=False)
    city_id = Column(Integer, ForeignKey(City.uid), nullable=False)
    places: RelationshipProperty = relationship('RoutePoint')

    def __str__(self) -> str:
        return 'Place {uid}, {name}'.format(
            uid=self.uid,
            name=self.name,
        )


class RoutePoint(Base):
    __tablename__ = 'routes_points'

    position = Column(Integer)
    place_id = Column(Integer, ForeignKey(Place.uid), nullable=False)
    route_id = Column(Integer, ForeignKey(Route.uid), nullable=False)
    distance = Column(Integer)
    place: RelationshipProperty = relationship('Place', lazy='joined')
    route: RelationshipProperty = relationship('Route', lazy='joined')

    __table_args__ = (
        UniqueConstraint(place_id, route_id),
        UniqueConstraint(position, route_id),
        PrimaryKeyConstraint(place_id, route_id, position),
    )

    def __str__(self) -> str:
        return 'Route: {route}, place: {place}'.format(
            route=self.route_id,
            place=self.place_id,
        )


class Travel(Base):
    __tablename__ = 'travels'

    uid = Column(Integer, primary_key=True)
    name = Column(String(), unique=True, nullable=False)
    city_id = Column(Integer, ForeignKey(City.uid), nullable=False)
    user_id = Column(Integer, ForeignKey(User.uid), nullable=False)

    def __str__(self) -> str:
        return 'Place {uid}, {name}'.format(
            uid=self.uid,
            name=self.name,
        )


def main():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()
