from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
def get_products():
    """Retrieves all available products."""
    return [{"message": "List of products will be here."}]
