from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from db.database import Base
from db.models.flight_model import flightModel

intpk = Annotated[int, mapped_column(primary_key=True)]

class ticketModel(Base):
    __tablename__ = "ticket"  

    id: Mapped[intpk]
    flight_id: Mapped[int] = mapped_column(ForeignKey("flight.id"))  # Внешний ключ
    seat: Mapped[str]
    price: Mapped[int]
    meal: Mapped[bool]
    is_booked: Mapped[bool]
    
    # Связь с моделью Passenger (ленивая загрузка по умолчанию)
    # flight: Mapped["flightModel"] = relationship(back_populates="ticket")

    # Альтернативный вариант с только прямой связью (без обратной)
    # flight: Mapped["flightModel"] = relationship()