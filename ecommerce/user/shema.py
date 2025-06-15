from pydantic import BaseModel, constr, EmailStr, ConfigDict


class User(BaseModel):
    name: constr(min_length=2, max_length=50)
    email: EmailStr
    password: str


class DisplayUser(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)