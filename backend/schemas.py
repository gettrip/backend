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


class Travel(Base):
    uid: int
    city_uid: int
    user_uid: int
    name: str = Field(min_length=1)
