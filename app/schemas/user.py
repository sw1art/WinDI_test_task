from pydantic import BaseModel, EmailStr, constr

class UserBase(BaseModel):
    name: constr(min_length=1, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    password: constr(min_length=8)

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
