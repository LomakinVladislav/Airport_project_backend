from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from db.orm.cashier_orm import add_cashier, get_cashiers
from db.schemas.cashier_schemas import CashierAddSchema
from db.database import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

router = APIRouter()

@router.post("/cashier")
async def add_cashier_api(data: CashierAddSchema, session: SessionDep):
    result = await add_cashier(data=data, session=session)
    return result

@router.get("/cashiers")
async def get_cashiers_api(session: SessionDep):
    result = await get_cashiers(session=session)
    return result