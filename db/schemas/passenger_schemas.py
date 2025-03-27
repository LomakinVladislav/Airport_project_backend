from pydantic import BaseModel

class PassengerAddSchema(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: str
    phone_number: str

class PassengerSchema(PassengerAddSchema):
    id: int

