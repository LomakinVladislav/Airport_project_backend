from pydantic import BaseModel

class CashierAddSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: str
    phone_number: str
    inn: str

class PassengerSchema(CashierAddSchema):
    id: int

