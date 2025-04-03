from pydantic import BaseModel

class TicketAddSchema(BaseModel):
    flight_id: int
    seat: str
    meal: bool
    price: int
    is_booked: bool

class TicketSchema(TicketAddSchema):
    id: int