from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]

class flightModel(Base):
    __tablename__ = "flight"  

    id: Mapped[intpk]
    departure_airport: Mapped[str]
    arrival_airport: Mapped[str]
    departure_time: Mapped[str] # Тут 
    arrival_time: Mapped[str] #  и тут найти нормальный формат для хранения даты 
