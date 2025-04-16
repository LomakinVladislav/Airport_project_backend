from pydantic import BaseModel

class TicketAddSchema(BaseModel):
    flight_id: int
    seat: str
    meal: bool
    price: int
    is_booked: bool

class TicketSchema(TicketAddSchema):
    id: int

class TicketSearchShema(BaseModel):
    id: int
    departure_time: str
    arrival_time: str
    ship_type: str
    number_of_seats: int
    price: int