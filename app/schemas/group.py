from pydantic import BaseModel, constr
from typing import List

class GroupCreate(BaseModel):
    name: constr(min_length=1, max_length=100)
    creator_id: int

class GroupResponse(BaseModel):
    id: int
    name: str
    creator_id: int
    users: List[int] = []

    class Config:
        from_attributes = True
