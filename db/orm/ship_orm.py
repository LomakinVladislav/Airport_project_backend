# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.ship_model import shipModel
from db.schemas.ship_schemas import ShipAddSchema


async def add_ship(data: ShipAddSchema, session: Session):
    new_ship = shipModel( 
        type=data.type,
        model=data.model,
        number_of_seats=data.number_of_seats,
    )
    session.add(new_ship)
    await session.commit()
    return {"ok": True}


async def get_ships(session: Session):
    query = select(shipModel)
    result = await session.execute(query)
    return result.scalars().all()
    