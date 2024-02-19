from sqlalchemy import create_engine, select, bindparam, func
from setting_database.db.core.initializer import create_connection
from db.models import *
from typing import List, Any, Dict
from schema import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_, and_
# from sqlalchemy.engine.result import ResultProxy
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
import datetime


class DML:
    @staticmethod
    def add_rents(session: Session, rent: RentInfo):
        try:
            if not session.query(BookTable).filter_by(bookid=rent.bookid).first():
                return {"error": "BookID not found"}
            if not session.query(UserTable).filter_by(userid=rent.userid).first():
                return {"error": "UserID not found"}
            
            status = session.query(BookTable).filter_by(bookid=rent.bookid).first().status
            if status == True:
                return {"error": "Book is renting"}
            new_rent = RentTable(
                userid=rent.userid,
                bookid=rent.bookid,
                expirationdate=rent.expirationdate,
            )
            session.query(BookTable).filter_by(bookid=rent.bookid).update({"status": True})
            session.add(new_rent)
            session.commit()
            return {"message": "successfully"}
        except Exception as e:
            error_message = str(e)
            return {"error": error_message}
        
    @staticmethod
    def return_rents(session: Session, rentid: int):
        try:
            if not session.query(RentTable).filter_by(rentid=rentid).first():
                return {"error": "RentID not found"}
            if session.query(RentTable).filter_by(rentid=rentid).first().returnday:
                return {"error": "RentID finish"}
            bookids = session.query(RentTable).filter_by(rentid=rentid).first()
            bookid = bookids.bookid
            session.query(BookTable).filter_by(bookid=bookid).update({"status": False})
            session.query(RentTable).filter_by(rentid=rentid).update({"returnday": func.now()})
            session.commit()
            return {"message": "successfully"}
        except Exception as e:
            error_message = str(e)
            return {"error": error_message}