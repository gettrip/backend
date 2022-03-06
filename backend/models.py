from sqlalchemy import Column, String
from backend.db import Base, engine


class City(Base):
    __tablename__ = 'cities'

    uid = Column(String(), primary_key=True)
    name = Column(String(), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'City {self.uid}, {self.name}'


def main():    
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()
