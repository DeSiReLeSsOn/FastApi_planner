from pydantic import BaseModel 
from typing import Optional, List 
from models.events import Event 


class User(BaseModel):
    email: EmailStr 
    password: str 
    events: Optional[List[Event]]

    class Config: 
        schema_extra = {
            "example": {
                "email": jonjones@gmail.com, 
                "username": "nigga", 
                "events": [],
            }
        } 


class UserSignIn(BaseModel):
    email: EmailStr 
    password: str 

    class Config:
        schema_extra = {
            "example": {
                "email": jonjones@gmail.com, 
                "password": "str", 
                "events": [],
            }
        }