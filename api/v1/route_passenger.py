from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from db.orm.passnger_orm import  add_passenger, get_passengers
from db.schemas.passenger_schemas import PassengerAddSchema
from db.database import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

router = APIRouter()


@router.post("/passenger")
async def add_passenger_api(data: PassengerAddSchema, session: SessionDep):
    result = await add_passenger(data=data, session=session)
    return result


@router.get("/passengers")
async def get_passengers_api(session: SessionDep):
    result = await get_passengers(session=session)
    return result