import datetime
from sqlalchemy import (
    Column, String, Integer, DateTime, ForeignKey, Boolean,
    Sequence, create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class BookTable(Base):
    __tablename__ = 'book'

    bookid = Column(Integer, Sequence('book_bookid'), primary_key=True)
    bookname = Column(String)
    author = Column(String)
    publishyear = Column(Integer)

    # Quan hệ với RentBook
    rentals = relationship("RentBook", back_populates="book")

class UserTable(Base):
    __tablename__ = 'user'

    userid = Column(Integer, Sequence('user_userid'), primary_key=True)
    username = Column(String)
    name = Column(String)
    password = Column(String)
    status = Column(Boolean)

    # Quan hệ với RentBook
    rentals = relationship("RentBook", back_populates="user")

class RentBook(Base):
    __tablename__ = 'rentbook'

    rentid = Column(Integer, Sequence('rentbook_rentid'), primary_key=True)
    book_bookid = Column(Integer, ForeignKey('book.bookid'))
    user_userid = Column(Integer, ForeignKey('user.userid'))
    dayofrenting = Column(DateTime)
    expirationdate = Column(DateTime)

    # Quan hệ với Book và User
    book = relationship("BookTable", back_populates="rentals")
    user = relationship("UserTable", back_populates="rentals")

