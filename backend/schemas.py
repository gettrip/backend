from  pydantic import BaseModel, constr

class City(BaseModel):        
    name: str
    name: constr(min_length=1)
        

    class Config:
        orm_mode=True
