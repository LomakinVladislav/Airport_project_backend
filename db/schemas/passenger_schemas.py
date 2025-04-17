from pydantic import BaseModel

class PassengerAddSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    birth_date: str
    gender: str
    passport: str
    phone_number: str

class PassengerSchema(PassengerAddSchema):
    id: int

