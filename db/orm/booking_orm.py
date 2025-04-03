# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.booking_model import bookingModel
from db.schemas.booking_schemas import BookingAddSchema

async def add_booking(data: BookingAddSchema, session: Session):
    new_booking = bookingModel( 
        is_bought=data.is_bought,
        ticket_id=data.ticket_id,
        cashier_id=data.cashier_id,
        passenger_id=data.passenger_id
    )
    session.add(new_booking)
    await session.commit()
    return {"ok": True}


async def get_bookings(session: Session):
    query = select(bookingModel)
    result = await session.execute(query)
    return result.scalars().all()
    