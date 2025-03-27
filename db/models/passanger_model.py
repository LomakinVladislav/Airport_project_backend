from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]

class passengerModel(Base):
    __tablename__ = "passenger"  

    id: Mapped[intpk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    age: Mapped[int]
    gender: Mapped[str]
    phone_number: Mapped[str]

