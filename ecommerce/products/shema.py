from pydantic import BaseModel, constr

class Category(BaseModel):
    name: constr(min_length=2, max_length=50)

class DisplayCategory(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True