from typing import Annotated
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]

class bookingModel(Base):
    __tablename__ = "booking"  

    id: Mapped[intpk]
    is_bought: Mapped[bool]
    ticket_id: Mapped[int] = mapped_column(ForeignKey("ticket.id"))  # Внешний ключ
    cashier_id: Mapped[int] = mapped_column(ForeignKey("cashier.id"))  # Внешний ключ
    passenger_id: Mapped[int] = mapped_column(ForeignKey("passenger.id"))  # Внешний ключ

    ticket = relationship("ticketModel", back_populates="booking")
    passenger = relationship("passengerModel", back_populates="booking")
    cashier = relationship("cashierModel", back_populates="booking")