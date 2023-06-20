from fastapi import APIRouter
from app.schemas import user as user_schema

router = APIRouter()

@router.post("/users/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate):
    # Your implementation here
    pass

@router.get("/users/{user_id}", response_model=user_schema.User)
def read_user(user_id: int):
    # Your implementation here
    pass
