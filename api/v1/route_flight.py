from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from db.orm.flight_orm import add_flight, get_flights
from db.schemas.flight_schemas import FlightAddSchema
from db.database import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

router = APIRouter()

@router.post("/flight")
async def add_flight_api(data: FlightAddSchema, session: SessionDep):
    result = await add_flight(data=data, session=session)
    return result

@router.get("/flights")
async def get_flights_api(session: SessionDep):
    result = await get_flights(session=session)
    return result