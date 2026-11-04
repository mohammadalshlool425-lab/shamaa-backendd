from app.models.user import UserCreate


def create_new_user(user_data: UserCreate):
    """
    Business logic for creating a user.
    Here you would typically hash passwords and interact with Supabase.
    """
    print(f"Creating user: {user_data.full_name}")
    return {
        "id": "mock-uuid-1234",
        "full_name": user_data.full_name,
        "email": user_data.email,
        "phone_number": user_data.phone_number,
        "is_yarmouk_student": user_data.is_yarmouk_student,
        "student_id": user_data.student_id,
        "verification_status": "unverified",
    }
