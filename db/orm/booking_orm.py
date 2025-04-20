# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.booking_model import bookingModel
from db.models.ticket_model import ticketModel
from db.schemas.booking_schemas import BookingAddSchema
from db.orm.passnger_orm import add_passenger
from db.schemas.passenger_schemas import PassengerAddSchema


async def get_ticket_id_by_flight_id_and_seat(flight_id: int, seat: str,  session: Session):
    query = select(ticketModel.id).filter(ticketModel.flight_id == flight_id, ticketModel.seat == seat)
    result = await session.execute(query)
    return result.scalars().first()


async def add_booking(data: BookingAddSchema, session: Session):

    # Добавить проверку на то, что пользователь уже существуют в БД
    passenger_data = PassengerAddSchema(**data.model_dump())

    # Вызвать функцию добавления пассажира
    passenger_id = await add_passenger(passenger_data, session=session)

    # Через flight_id и seat из BookingAddThroughPassengerShema получить из БД ticket_id
    ticket_id = await get_ticket_id_by_flight_id_and_seat(data.flight_id, data.seat, session=session)
 
    # 3. Передать ticket_id и passnger_id в функцию ниже:

    new_booking = bookingModel( 
        is_bought=False,
        ticket_id=ticket_id,
        cashier_id=1,
        passenger_id=passenger_id
    )
    session.add(new_booking)
    await session.commit()
    await session.refresh(new_booking)
    return {"booking_id": new_booking.id}


async def get_bookings(session: Session):
    query = select(bookingModel)
    result = await session.execute(query)
    return result.scalars().all()
    