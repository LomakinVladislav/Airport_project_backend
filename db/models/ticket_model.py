from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from db.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]

class ticketModel(Base):
    __tablename__ = "ticket"  

    id: Mapped[intpk]
    seat: Mapped[str]
    price: Mapped[int]
    is_booked: Mapped[bool]
    flight_id: Mapped[int] = mapped_column(ForeignKey("flight.id"))  # Внешний ключ

    flight = relationship("flightModel", back_populates="ticket")
    booking = relationship("bookingModel", back_populates="ticket")
