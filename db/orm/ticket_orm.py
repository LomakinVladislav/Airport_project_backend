# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.ticket_model import ticketModel
from db.schemas.ticket_schemas import TicketAddSchema

async def add_ticket(data: TicketAddSchema, session: Session):
    new_ticket = ticketModel( 
        flight_id = data.flight_id,
        seat = data.seat,
        price = data.price,
        meal = data.meal,
        is_booked = data.is_booked
    )
    session.add(new_ticket)
    await session.commit()
    return {"ok": True}


async def get_tickets(session: Session):
    query = select(ticketModel)
    result = await session.execute(query)
    return result.scalars().all()
    