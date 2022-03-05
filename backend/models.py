from sqlalchemy import Column, String
from backend.db import Base, engine


class City(Base):
    __tablename__ = 'cities'

    uid = Column(String(), primary_key=True)
    name = Column(String(), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'User {self.uid}, {self.name}'


class User(Base):
    __tablename__ = 'users'

    uid = Column(String(), primary_key=True)
    name = Column(String(), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'User {self.uid}, {self.name}'


def main():    
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()