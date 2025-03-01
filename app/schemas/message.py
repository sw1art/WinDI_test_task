from pydantic import BaseModel, constr
from datetime import datetime

class MessageBase(BaseModel):
    text: constr(min_length=1, max_length=1000)
    is_read: bool = False

class MessageCreate(MessageBase):
    chat_id: int
    sender_id: int

class MessageResponse(MessageBase):
    id: int
    chat_id: int
    sender_id: int
    timestamp: datetime

    class Config:
        from_attributes = True
