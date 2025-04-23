# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import select, insert, update
from sqlalchemy.orm import Session
import random

from db.models.ticket_model import ticketModel
from db.models.flight_model import flightModel
from db.models.ship_model import shipModel
from db.schemas.ticket_schemas import TicketAddSchema

async def add_ticket(data: TicketAddSchema, session: Session):
    new_ticket = ticketModel( 
        flight_id = data.flight_id,
        seat = data.seat,
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
        flightModel.departure_airport,
        flightModel.arrival_airport,
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


async def generate_tickets(session: Session, flight_id: int, number_of_seats: int) -> None:
    seats = []
    # Определяем набор букв для мест
    if number_of_seats < 10:
        letters = ['A', 'B']
    elif number_of_seats < 100:
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
    else:
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    
    for i in range(number_of_seats):
        # Вычисляем номер ряда и букву места
        row_number = (i // len(letters)) + 1
        letter = letters[i % len(letters)]
        seat = f"{letter}{row_number}"
        
        # Генерируем случайную цену от 100 до 500
        price = random.randint(100, 500)
        
        seats.append({
            "seat": seat,
            "price": price,
            "is_booked": False,
            "flight_id": flight_id
        })

    # Массовая вставка записей
    await session.execute(
        insert(ticketModel), 
        seats
    )
    await session.commit()


async def check_ticket_status(ticket_id: int, session: Session):
    query = (select(ticketModel.is_booked)
    .where(ticketModel.id == ticket_id))
    result = await session.execute(query)
    return result.scalars().first()


async def change_ticket_status(ticket_id: int, session: Session):

    query = (update(ticketModel)
    .where(ticketModel.id == ticket_id)
    .values(is_booked=True))

    await session.execute(query)
    await session.commit()
    

async def get_available_tickets(flight_id: int, session: Session):
    query = (select(ticketModel.seat)
    .where(ticketModel.flight_id == flight_id))
    result = await session.execute(query)
    return result.scalars().all()