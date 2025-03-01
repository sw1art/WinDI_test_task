from pydantic import BaseModel, constr

class ChatBase(BaseModel):
    name: constr(min_length=1, max_length=100)
    is_group: bool

class ChatCreate(ChatBase):
    pass

class ChatResponse(ChatBase):
    id: int

    class Config:
        from_attributes = True
