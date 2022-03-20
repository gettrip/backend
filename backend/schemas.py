from pydantic import BaseModel, Field


class Base(BaseModel):

    class Config:
        orm_mode = True


class City(Base):
    uid: int
    name: str = Field(min_length=1)


class User(Base):
    username: str = Field(min_length=1)


class Place(Base):
    uid: int
    city_uid: int
    name: str = Field(min_length=1)


class Travel(Base):
    uid: int
    city_uid: int
    user_uid: int
    name: str = Field(min_length=1)
