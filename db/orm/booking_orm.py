# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.booking_model import bookingModel
from db.models.ticket_model import ticketModel
from db.models.passanger_model import passengerModel
from db.models.flight_model import flightModel
from db.schemas.booking_schemas import BookingAddSchema
from db.orm.passnger_orm import add_passenger, get_passenger_id
from db.orm.ticket_orm import change_ticket_status_true, check_ticket_status, change_ticket_status_false
from db.schemas.passenger_schemas import PassengerAddSchema


async def get_ticket_id_by_flight_id_and_seat(flight_id: int, seat: str,  session: Session):
    query = select(ticketModel.id).filter(ticketModel.flight_id == flight_id, ticketModel.seat == seat)
    result = await session.execute(query)
    return result.scalars().first()


async def add_booking(data: BookingAddSchema, session: Session):

    # Добавить проверку на то, что пользователь уже существуют в БД
    passenger_data = PassengerAddSchema(**data.model_dump())
    
    passenger_id = await get_passenger_id(passenger_data.passport, session=session)
    if passenger_id == None:    
        # Вызвать функцию добавления пассажира
        passenger_id = await add_passenger(passenger_data, session=session)
        

    # Через flight_id и seat из BookingAddThroughPassengerShema получить из БД ticket_id
    ticket_id = await get_ticket_id_by_flight_id_and_seat(data.flight_id, data.seat, session=session)
    ticket_status = await check_ticket_status(ticket_id=ticket_id, session=session)
    
    if ticket_status:
        return "Ошибка: этот билет уже забронирован"
    else:
        await change_ticket_status_true(ticket_id=ticket_id, session=session)
        
    # Передать ticket_id и passnger_id в функцию ниже:

    new_booking = bookingModel( 
        is_bought=False,
        ticket_id=ticket_id,
        cashier_id=1,
        passenger_id=passenger_id
    )
    session.add(new_booking)
    await session.commit()
    await session.refresh(new_booking)
    # Функция записывающая, что билет забронирован в таблице tickets

    return {"booking_id": new_booking.id}


async def get_bookings(session: Session):
    query = select(bookingModel)
    result = await session.execute(query)
    return result.scalars().all()
    

async def search_bookings(passport: str, session: Session):
    query = (select(flightModel.departure_airport,
                    flightModel.arrival_airport,
                    flightModel.departure_date,
                    ticketModel.seat,
                    bookingModel.id.label("booking_id"))
                    .select_from(passengerModel)
                    .join(bookingModel).join(ticketModel).join(flightModel)
                    .filter(passengerModel.passport == passport))
    result = await session.execute(query)
    print(query)
    return result.mappings().all()


async def delete_booking(booking_id, session: Session):
    query = select(bookingModel).where(bookingModel.id == booking_id)
    result = await session.execute(query)
    booking_to_delete = result.scalars().first()

    if not booking_to_delete:
        return {"ok": False, "error": "Booking not found"}
    
    ticket_id = booking_to_delete.ticket_id

    await session.delete(booking_to_delete)
    await session.commit()

    await change_ticket_status_false(ticket_id=ticket_id, session=session)
    return {"ok": True}