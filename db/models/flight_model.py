from typing import Annotated
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.database import Base
from db.models.ship_model import shipModel

intpk = Annotated[int, mapped_column(primary_key=True)]

class flightModel(Base):
    __tablename__ = "flight"  

    id: Mapped[intpk]
    departure_airport: Mapped[str]
    arrival_airport: Mapped[str]
    departure_time: Mapped[str] # Тут 
    arrival_time: Mapped[str] #  и тут найти нормальный формат для хранения даты 
    ship_id: Mapped[int] = mapped_column(ForeignKey("ship.id"))  # Внешний ключ
