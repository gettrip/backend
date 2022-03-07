from  pydantic import BaseModel

class CitySchema(BaseModel):
    uid: str
    name: str
    description: str
    