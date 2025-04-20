from pydantic import BaseModel
from db.schemas.passenger_schemas import PassengerAddSchema

class BookingAddSchema(PassengerAddSchema):
    flight_id: int
    seat: str

class BookingSchema(BookingAddSchema):
    id: int