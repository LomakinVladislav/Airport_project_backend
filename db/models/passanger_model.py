from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]

class passengerModel(Base):
    __tablename__ = "passenger"  

    id: Mapped[intpk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    middle_name: Mapped[str]
    birth_date: Mapped[str]
    gender: Mapped[str]
    passport: Mapped[str]
    phone_number: Mapped[str]

