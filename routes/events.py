from fastapi import APIRouter, HTTPException, status, Request, Depends
from models.events import Event 
from typing import List 
from database.connection import get_session 
from models.events import Event, EventUpdate 
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


event_router = APIRouter(
    tags=["Events"]
) 


events = []


@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session: AsyncSession = Depends(get_session)) -> List[Event]:
    statement = select(Event)
    results = session.execute(statement)
    events = results.scalars().all()
    return events 


@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Event with supplied ID doesn't exist"
    )


@event_router.post("/new")
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {
        "message": "Event created successfully"
    }



@event_router.put("/edit/{id}")
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
            session.add(event)
            session.commit()
            session.refresh(event)

            return event 
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )



@event_router.delete("/{id}")
async def delete_event(id: int, session=Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit() 

        return {
            "message": "Event deleted successfully"
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID doen't exist"
    )


@event_router.delete("/")
async def delete_all_events() -> dict: 
    events.clear()
    return {
        "message": "Events deleted successfully"
    }