from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.get("/")
def test():
    return {"message": "Auth Ready"}
