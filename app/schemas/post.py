from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    owner_id: int
    created_date: datetime

    class Config:
        orm_mode = True
