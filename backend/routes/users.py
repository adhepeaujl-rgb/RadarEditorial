from fastapi import APIRouter
from backend.models.user import User

router = APIRouter()

@router.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "status": "active"}

@router.post("/users/")
def create_user(user: User):
    return {"message": f"Utilisateur {user.name} créé avec succès"}
