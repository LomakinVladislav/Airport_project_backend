from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from db.database import Base
from db.models.flight_model import flightModel

intpk = Annotated[int, mapped_column(primary_key=True)]

class ticketModel(Base):
    __tablename__ = "ticket"  

    id: Mapped[intpk]
    seat: Mapped[str]
    meal: Mapped[bool]
    price: Mapped[int]
    is_booked: Mapped[bool]
    flight_id: Mapped[int] = mapped_column(ForeignKey("flight.id"))  # Внешний ключ
