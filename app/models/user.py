from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: Optional[str] = None
    is_yarmouk_student: bool = False
    student_id: Optional[str] = None


class UserResponse(UserCreate):
    id: str
    verification_status: str
