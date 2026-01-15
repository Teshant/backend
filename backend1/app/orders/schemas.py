from pydantic import BaseModel

class OrderCreate(BaseModel):
    pass

class OrderOut(BaseModel):
    id: int
    status: str
