from sqlalchemy import Column, Integer, String

from backend.db import Base, engine


class City(Base):
    __tablename__ = 'cities'

    uid = Column(Integer, primary_key=True)
    name = Column(String(), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'City {self.uid}, {self.name}'


class User(Base):
    __tablename__ = 'users'

    uid = Column(Integer, primary_key=True)
    username = Column(String(), unique=True)

    def __repr__(self) -> str:
        return f'User {self.uid}, {self.username}'


class Place(Base):
    __tablename__ = 'places'

    uid = Column(Integer, primary_key=True)
    city_uid = Column(Integer, nullable=False)
    name = Column(String(), nullable=False)

    def __repr__(self) -> str:
        return f'Place {self.uid}, {self.name}'


def main():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()
