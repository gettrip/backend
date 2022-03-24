from pydantic import BaseModel, Field


class Schema(BaseModel):

    class Config:
        orm_mode = True


class City(Schema):
    uid: int
    name: str = Field(min_length=1)


class User(Schema):
    username: str = Field(min_length=1)


class Place(Schema):
    uid: int
    city_id: int
    name: str = Field(min_length=1)


class Route(Schema):
    uid: int
    city_id: int
    name: str = Field(min_length=1)


class RoutePlace(Schema):
    position: int
    place_id: int
    route_id: int
    distance: int


class Travel(Schema):
    uid: int
    city_id: int
    user_id: int
    name: str = Field(min_length=1)
