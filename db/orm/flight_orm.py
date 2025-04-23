# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.flight_model import flightModel
from db.models.ship_model import shipModel
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
    

async def search_flights(departure_airport, arrival_airport, departure_date, session: Session):
    query = (select(flightModel.id.label("flight_id"),
                    flightModel.departure_airport,
                    flightModel.arrival_airport,
                    flightModel.departure_date,
                    flightModel.arrival_date,
                    flightModel.departure_time,
                    flightModel.arrival_time,
                    shipModel.type.label("ship_type"),
                    shipModel.number_of_seats).select_from(flightModel)
                    .join(shipModel)
                    .filter(flightModel.departure_airport == departure_airport)
                    .filter(flightModel.arrival_airport == arrival_airport)
                    .filter(flightModel.departure_date == departure_date))
    result = await session.execute(query)
    print(query)
    return result.mappings().all()