from sqlalchemy import Column, ForeignKey, Integer, String

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

    def __str__(self) -> str:
        return 'Place {uid}, {city_id}, {name}'.format(
            uid=self.uid,
            city_id=self.city_id,
            name=self.name,
        )


class Travel(Base):
    __tablename__ = 'travels'

    uid = Column(Integer, primary_key=True)
    name = Column(String(), unique=True, nullable=False)
    city_id = Column(Integer, ForeignKey(City.uid), nullable=False)
    user_id = Column(Integer, ForeignKey(User.uid), nullable=False)

    def __str__(self) -> str:
        return 'Place {uid}, {city_id}, {user_id}, {name}'.format(
            uid=self.uid,
            city_id=self.city_id,
            user_id=self.user_id,
            name=self.name,
        )


def main():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()
