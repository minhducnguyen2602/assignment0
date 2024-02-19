from sqlalchemy import create_engine, select, bindparam
from setting_database.db.core.initializer import create_connection
from db.models.model import *
from typing import List, Any, Dict
from schema import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_, and_
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
class DML:
    @staticmethod
    def add_users(session: Session, user: UserInfo):
        try:
            
            new_user = UserTable(
                username=user.username,
                dateofbirth = user.dateofbirth
            )

            session.add(new_user)
            session.commit()
            return {"message": "User registered successfully"}
        except SQLAlchemyError as e:
            # Handle the error and return the response
            error_message = str(e)
            return {"error": error_message}
    @staticmethod
    def update_users(id, session: Session, user: UserInfo):
        try:
            if not session.query(UserTable).filter_by(userid=id).first():
                return {"error": "UserID not found"}
            
            update_data = {}

            if user.username != "":
                update_data['username'] = user.username
            if user.dateofbirth:
                update_data['dateofbirth'] = user.dateofbirth
    

            session.query(UserTable).filter_by(userid=id).update(update_data)

            # session.query(BookTable).filter_by(bookid=book_id).update(**book.model_dump())

            session.commit()
            return {"message": "user updated successfully"}
        except Exception as e:
            error_message = str(e)
            return {"error": error_message}
