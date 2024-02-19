from sqlalchemy import create_engine, select, bindparam
from setting_database.db.core.initializer import create_connection
from db.models import *
from typing import List, Any, Dict
from schema import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_, and_
# from sqlalchemy.engine.result import ResultProxy
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload   
from sqlalchemy import func
class DML:
    @staticmethod
    def query_rentalhistory_books(session: Session, id: int):
        try:
            if not session.query(BookTable).filter_by(bookid=id).first():
                return {"error": "BookID not found"}
            if not session.query(RentTable).filter_by(bookid=id).first():
                return {"error": "BookID rental history not found"}
            result = session.query(BookTable, RentTable, UserTable).select_from(BookTable).join(RentTable).join(UserTable).filter(RentTable.bookid==id).all()
            # result_json = [row for row in result]
            if not result:
                return {"result": []}
            result_json = [
            {
                'Book name': book.bookname,
                'Book author': book.author,
                'User rent': user.username,
                'Day of rent': rent.dayofrent.strftime('%Y-%m-%d %H:%M:%S'),
                'Exprience Day': rent.expirationdate.strftime('%Y-%m-%d %H:%M:%S')
            }
            for book, rent, user in result
        ]
            return {"result": result_json}
        except Exception as e:
            error_message = str(e)
            return {"error": error_message}
    @staticmethod
    def query_rentalhistory_users(session: Session, id: int):
        try:

            if not session.query(UserTable).filter_by(userid=id).first():
                return {"error": "UserID not found"}
            if not session.query(RentTable).filter_by(userid=id).first():
                return {"error": "UserID rental history not found"}
            result = session.query(UserTable, RentTable, BookTable).select_from(UserTable).join(RentTable).join(BookTable).filter(RentTable.userid==id).all()
            # result_json = [row for row in result]
            result_json = [
            {
                'User rent': user.username,
                'Book name': book.bookname,
                'Book author': book.author,
                'Day of rent': rent.dayofrent.strftime('%Y-%m-%d %H:%M:%S'),
                'Exprience Day': rent.expirationdate.strftime('%Y-%m-%d %H:%M:%S')
            }
            for user, rent, book in result
        ]
            return {"result": result_json}
        except Exception as e:
            error_message = str(e)
            return {"error": error_message}
    @staticmethod
    def query_rental_of_categories(session: Session):
        try:
            rental_counts = (
                            session.query(BookTable.category, func.count(RentTable.rentid).label('rent_count'))
                            .join(RentTable, BookTable.bookid == RentTable.bookid)
                            .group_by(BookTable.category)
                            .all()
                            )
            rental_counts = [{'category': category, 'rent_count': rent_count} for category, rent_count in rental_counts]
            # Now, you can iterate through `rental_counts` to get the count for each category
            for category, count in rental_counts:
                books_in_category = session.query(BookTable).filter_by(category=category).all()
                for book in books_in_category:
                    book.rental_count = count

            return {"result": rental_counts}
        except Exception as e:
            error_message = str(e)
            return {"error": error_message}