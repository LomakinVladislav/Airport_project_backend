from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]

class cashierModel(Base):
    __tablename__ = "cashier"  

    id: Mapped[intpk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    middle_name: Mapped[str]
    phone_number: Mapped[str]
    inn: Mapped[str]
