from pydantic import BaseModel, Field


class City(BaseModel):
    uid: int
    name: str = Field(min_length=1)

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str = Field(min_length=1)

    class Config:
        orm_mode = True
