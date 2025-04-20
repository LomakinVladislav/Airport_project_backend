# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.flight_model import flightModel
from db.database import Base, async_engine
from db.schemas.flight_schemas import FlightAddSchema
from db.orm.ticket_orm import generate_tickets
from db.orm.ship_orm import get_number_of_seats_by_ship_id


async def add_flight(data: FlightAddSchema, session: Session):
    new_flight = flightModel( 
        departure_airport=data.departure_airport,
        arrival_airport=data.arrival_airport,
        departure_date=data.departure_date,
        departure_time=data.departure_time,
        arrival_date=data.arrival_date,
        arrival_time=data.arrival_time,
        ship_id = data.ship_id
    )
    session.add(new_flight)
    await session.commit()
    await session.refresh(new_flight)

    flight_id = new_flight.id
    number_of_seats = await get_number_of_seats_by_ship_id(data.ship_id, session=session)
    await generate_tickets(flight_id=flight_id, number_of_seats=number_of_seats, session=session)

    return {"ok": True}


async def get_flights(session: Session):
    query = select(flightModel)
    result = await session.execute(query)
    return result.scalars().all()
    