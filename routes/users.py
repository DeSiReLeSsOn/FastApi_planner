from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn


user_router = APIRouter(
    tags=["User"]
)


users = {}

@user_router.post("/singup")
async def sign_new_user(data: NewUser) ->dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            details="User with supplid username exists"
        )
    users[data.email] = data 
    return {
        "message": "user successfully registered!"
    }
