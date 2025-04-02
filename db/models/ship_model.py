from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]

class shipModel(Base):
    __tablename__ = "ship"  

    id: Mapped[intpk]
    type: Mapped[str]
    model: Mapped[str]
    number_of_seats: Mapped[int]