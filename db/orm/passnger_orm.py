# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.passanger_model import passengerModel
from db.schemas.passenger_schemas import PassengerAddSchema


async def add_passenger(data: PassengerAddSchema, session: Session):
    new_passenger = passengerModel(**data.model_dump())
    session.add(new_passenger)
    await session.commit()
    await session.refresh(new_passenger)
    return new_passenger.id


async def get_passengers(session: Session):
    query = select(passengerModel)
    result = await session.execute(query)
    return result.scalars().all()


async def get_passenger_id(passport: str, session: Session):
    query = select(passengerModel.id).where(passengerModel.passport == passport)
    result = await session.execute(query)
    return result.scalars().first()