from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from db.orm.ticket_orm import add_ticket, get_tickets
from db.schemas.ticket_schemas import TicketAddSchema
from db.database import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

router = APIRouter()

@router.post("/ticket")
async def add_ticket_api(data: TicketAddSchema, session: SessionDep):
    result = await add_ticket(data=data, session=session)
    return result

@router.get("/tickets")
async def get_tickets_api(session: SessionDep):
    result = await get_tickets(session=session)
    return result