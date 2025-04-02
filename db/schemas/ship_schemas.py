from pydantic import BaseModel

class ShipAddSchema(BaseModel):
    type: str
    model: str
    number_of_seats: int

class ShipSchema(ShipAddSchema):
    id: int

