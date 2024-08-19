from pydantic import BaseModel 
from typing import List 


class Event(BaseModel):
    id: int
    title: str 
    image: str 
    description: str 
    tags: List[str]
    location: str 

    class Config:
        schema_extra = {
            "example": {
                "title": "FastApi Studying", 
                "image": "https://linktomyimage.com/image.png", 
                "description": "Great", 
                "tags": ["python", "fastapi", "golang", "net/http"], 
                "location": "Chistyakove"
            }
        }