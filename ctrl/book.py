from sqlalchemy import create_engine, select, bindparam
from setting_database.db.core.initializer import create_connection
from db.models import *
from typing import List, Any, Dict
from schema import BookInfo
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_, and_
# from sqlalchemy.engine.result import ResultProxy
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session


class DML:
    @staticmethod
    def add_books(session: Session, book: BookInfo):
        try:
            new_book = BookTable(**book.model_dump())
            session.add(new_book)
            session.commit()
            return {"message": "Book added successfully"}
        except Exception as e:
            error_message = str(e)
            return {"error": error_message}

    @staticmethod
    def delete_books(session: Session, book_id: int):
        try:
            if not session.query(BookTable).filter_by(bookid=book_id).first():
                return {"error": "BookID not found"}
            if session.query(RentTable).filter_by(bookid=book_id).first():
                return {"error": "BookID was rented"}
            session.query(BookTable).filter_by(bookid=book_id).delete()
            session.commit()
            return {"message": "Book deleted successfully"}
        except Exception as e:
            error_message = str(e)
            return {"error": error_message}

    @staticmethod
    def update_books_info(session: Session, book_id: int, book: BookInfo):
        try:
            if not session.query(BookTable).filter_by(bookid=book_id).first():
                return {"error": "BookID not found"}
            update_data = {}

            if book.bookname != "":
                update_data['bookname'] = book.bookname
            if book.author != "":
                update_data['author'] = book.author
            if book.category != "":
                update_data['category'] = book.category
            if book.publishyear != -1:
                update_data['publishyear'] = book.publishyear

            session.query(BookTable).filter_by(bookid=book_id).update(update_data)

            # session.query(BookTable).filter_by(bookid=book_id).update(**book.model_dump())

            session.commit()
            return {"message": "Book updated successfully"}
        except Exception as e:
            error_message = str(e)
            return {"error": error_message}

    @staticmethod
    def query_books_info(session: Session, book: BookInfo):
        try:
            conditions = []

            if book.bookname != "":
                conditions.append(BookTable.bookname == book.bookname)
            if book.author != "":
                conditions.append(BookTable.author == book.author)
            if book.category != "":
                conditions.append(BookTable.category == book.category)    
            if book.publishyear != -1:
                conditions.append(BookTable.publishyear == book.publishyear)

            query = session.query(BookTable).filter(*conditions) if conditions else session.query(BookTable)
            result = query.all()

            result_json = [row.__dict__ for row in result]

            return {"result": result_json}
        except Exception as e:
            error_message = str(e)
            return {"error": error_message}

    @staticmethod
    def query_all_books(session: Session):
        try:
            query = session.query(BookTable)
            result = query.all()

            result_json = [row.__dict__ for row in result]

            return {"result": result_json}
        except Exception as e:
            error_message = str(e)
            return {"error": error_message}

   