from  pydantic import BaseModel, constr

class City(BaseModel):    
    uid: int
    name: constr(min_length=1)    
      

    class Config:
        orm_mode=True

class User(BaseModel):
    name: constr(min_length=1)

    class Config:
        orm_mode=True
