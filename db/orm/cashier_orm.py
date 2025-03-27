# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import select
from sqlalchemy.orm import Session

from db.models.cashier_model import cashierModel
from db.database import Base, async_engine
from db.schemas.cashier_schemas import CashierAddSchema


async def add_cashier(data: CashierAddSchema, session: Session):
    new_cashier = cashierModel( 
        first_name=data.first_name,
        last_name=data.last_name,
        phone_number=data.phone_number,
        inn=data.inn
    )
    session.add(new_cashier)
    await session.commit()
    return {"ok": True}


async def get_cashiers(session: Session):
    query = select(cashierModel)
    result = await session.execute(query)
    return result.scalars().all()
    