from pydantic import BaseModel

class BookingAddSchema(BaseModel):
    is_bought: bool
    ticket_id: int
    cashier_id: int
    passenger_id: int

class BookingSchema(BookingAddSchema):
    id: int