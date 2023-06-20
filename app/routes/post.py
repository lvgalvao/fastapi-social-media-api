from fastapi import APIRouter
from app.schemas import post as post_schema

router = APIRouter()

@router.post("/posts/", response_model=post_schema.Post)
def create_post(post: post_schema.PostCreate):
    # Your implementation here
    pass

@router.get("/posts/{post_id}", response_model=post_schema.Post)
def read_post(post_id: int):
    # Your implementation here
    pass
