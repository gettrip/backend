from pydantic import BaseModel, Field


class Schema(BaseModel):

    class Config:
        orm_mode = True


class City(Schema):
    uid: int
    name: str = Field(min_length=1)
    image: str


class User(Schema):
    username: str = Field(min_length=1)


class Place(Schema):
    uid: int
    city_id: int
    name: str = Field(min_length=1)
    image: str
    description: str
    duration: int


class Route(Schema):
    uid: int
    city_id: int
    name: str = Field(min_length=1)
    image: str
    description: str
    duration: int


class RoutePoint(Schema):
    position: int
    distance: int
    place: Place


class Travel(Schema):
    uid: int
    city_id: int
    user_id: int
    name: str = Field(min_length=1)
