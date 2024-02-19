
from . import Base
import datetime
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, create_engine, Sequence, DateTime, func
from sqlalchemy.orm import validates
from sqlalchemy.orm import Session
from database import get_db

from fastapi import Depends



class BookTable(Base):
    __tablename__ = 'book'

    bookid: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement= True)
    bookname: Mapped[Optional[str]]
    author: Mapped[Optional[str]]
    category: Mapped[Optional[str]]
    publishyear: Mapped[Optional[int]] 
    status: Mapped[bool] = mapped_column(default=False)

    # rent: Mapped[List["RentTable"]] = relationship(back_populates="book")


class UserTable(Base):
    __tablename__ = 'user'

    userid: Mapped[int] = mapped_column(primary_key=True, autoincrement = True)
    username : Mapped[Optional[str]]
    dateofbirth: Mapped[Optional[datetime.date]]


class RentTable(Base):
    __tablename__ = 'rentbook'

    rentid : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    bookid : Mapped[int] = mapped_column(ForeignKey("book.bookid"))
    userid : Mapped[int] = mapped_column(ForeignKey("user.userid"))
    dayofrent : Mapped[datetime.date] = mapped_column(DateTime(), server_default=func.now())
    expirationdate : Mapped[datetime.date]
    returnday: Mapped[Optional[datetime.date]]

    # book: Mapped[List["BookTable"]] = relationship(back_populates="rent")
        
    @validates("expirationdate")
    def validate_expirationdate(self, key, value):
        # Thêm logic kiểm tra ngày hết hạn ở đây
        if value < datetime.datetime.now().date():
            raise ValueError("ERROR: Expiration date must be after the rental date.")
        return value




