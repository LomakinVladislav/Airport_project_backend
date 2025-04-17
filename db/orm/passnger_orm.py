# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.passanger_model import passengerModel
from db.database import Base, async_engine
from db.schemas.passenger_schemas import PassengerAddSchema


async def add_passenger(data: PassengerAddSchema, session: Session):
    new_passenger = passengerModel( 
        first_name=data.first_name,
        last_name=data.last_name,
        middle_name = data.middle_name,
        birth_date = data.birth_date,
        gender=data.gender,
        passport = data.passport,
        phone_number = data.phone_number
    )
    session.add(new_passenger)
    await session.commit()
    return {"ok": True}


async def get_passengers(session: Session):
    query = select(passengerModel)
    result = await session.execute(query)
    return result.scalars().all()
    