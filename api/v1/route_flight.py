from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from db.orm.flight_orm import add_flight, get_flights, search_flights
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


@router.get("/search_flights")
async def search_flights_api(departure_airport: str, arrival_airport: str, departure_date: str, session: SessionDep):
    result = await search_flights(departure_airport=departure_airport, arrival_airport=arrival_airport,\
                                   departure_date=departure_date, session=session)
    return result