from pydantic import BaseModel

class TicketAddSchema(BaseModel):
    flight_id: int
    seat: str
    price: int
    meal: bool
    is_booked: bool

class TicketSchema(TicketAddSchema):
    id: int