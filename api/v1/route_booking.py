from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from db.orm.booking_orm import add_booking, get_bookings
from db.schemas.booking_schemas import BookingAddSchema
from db.database import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

router = APIRouter()

@router.post("/booking")
async def add_booking_api(data: BookingAddSchema, session: SessionDep):
    result = await add_booking(data=data, session=session)
    return result

@router.get("/bookings")
async def get_bookings_api(session: SessionDep):
    result = await get_bookings(session=session)
    return result