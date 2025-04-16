from pydantic import BaseModel

class FlightAddSchema(BaseModel):
    departure_airport: str
    arrival_airport: str
    departure_date: str
    departure_time: str # Тут 
    arrival_date: str
    arrival_time: str #  и тут найти нормальный формат для хранения даты 
    ship_id: int

class FlightSchema(FlightAddSchema):
    id: int

