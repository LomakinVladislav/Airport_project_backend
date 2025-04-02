from pydantic import BaseModel

class FlightAddSchema(BaseModel):
    departure_airport: str
    arrival_airport: str
    departure_time: str # Тут 
    arrival_time: str #  и тут найти нормальный формат для хранения даты 

class FlightSchema(FlightAddSchema):
    id: int

