from sqlalchemy import Column, String
from backend.db import Base, engine


class City(Base):
    __tablename__ = 'cities'

    id = Column(String(), primary_key=True)
    cityname = Column(String(), unique=True)

    def __repr__(self) -> str:
        return f'User {self.id}, {self.cityname}'
        

def main():    
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()