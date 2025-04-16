# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.ticket_model import ticketModel
from db.models.flight_model import flightModel
from db.models.ship_model import shipModel
from db.schemas.ticket_schemas import TicketAddSchema

async def add_ticket(data: TicketAddSchema, session: Session):
    new_ticket = ticketModel( 
        flight_id = data.flight_id,
        seat = data.seat,
        meal = data.meal,
        price = data.price,
        is_booked = data.is_booked
    )
    session.add(new_ticket)
    await session.commit()
    return {"ok": True}


async def get_tickets(session: Session):
    query = select(ticketModel)
    result = await session.execute(query)
    return result.scalars().all()
    
async def search_tickets(departure_airport, arrival_airport, departure_date, session: Session):
    query = select(flightModel.id.label("flight_id"),
        flightModel.departure_time,
        flightModel.arrival_time,
        shipModel.type.label("ship_type"),
        shipModel.number_of_seats,
        ticketModel.price).select_from(ticketModel).join(flightModel)\
    .join(shipModel).filter(flightModel.departure_airport == departure_airport)\
    .filter(flightModel.arrival_airport == arrival_airport).filter(flightModel.departure_date == departure_date)
    result = await session.execute(query)
    print(query)
    return result.mappings().all()