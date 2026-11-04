from fastapi import APIRouter, HTTPException

from app.models.user import UserCreate, UserResponse
from app.services.user_service import create_new_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate):
    """Registers a new user (Student or Irbid Resident)."""
    try:
        return create_new_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
