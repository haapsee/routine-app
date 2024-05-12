from typing import List
from sqlalchemy  import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class User(Base):
    __tablename__ = 'user_account'

    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(64))
    lastname: Mapped[str] = mapped_column(String(64))
    email: Mapped[str] = mapped_column(String(128))
    password: Mapped[str] = mapped_column(String(128))

    tasks: Mapped[List['Task']] = relationship(back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return "User(id=%s, firstname=%s, lastname=%s, email=%s, passhash=%s)" % (self.id, self.firstname, self.lastname, self.email, self.password)
