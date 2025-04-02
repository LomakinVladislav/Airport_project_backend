from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from db.orm.ship_orm import add_ship, get_ships
from db.schemas.ship_schemas import ShipAddSchema
from db.database import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

router = APIRouter()

@router.post("/ship")
async def add_ship_api(data: ShipAddSchema, session: SessionDep):
    result = await add_ship(data=data, session=session)
    return result

@router.get("/ships")
async def get_ships_api(session: SessionDep):
    result = await get_ships(session=session)
    return result