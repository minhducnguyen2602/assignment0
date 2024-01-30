from sqlalchemy import create_engine, select, bindparam
from setting_database.db.core.initializer import create_connection
from model import *
from typing import List, Any, Dict
from schema import BookInfo
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_, and_
# from sqlalchemy.engine.result import ResultProxy
from sqlalchemy.engine import Result
class DML:
    @staticmethod
    def add_books(book: BookInfo):
        try:
            statement = BookTable.insert().values(
                bookname=book.book_name,
                author=book.author,
                publishyear=book.publish_year
            )
            with create_connection() as conn:
                conn.execute(statement)
            return {"message": "Book added successfully"}
        except SQLAlchemyError as e:
            # Xử lý lỗi và trả về phản hồi
            error_message = str(e)
            return {"error": error_message}
    @staticmethod
    def delete_books(id:int):
        try:
            statement = BookTable.delete().where(
                    BookTable.bookid==bindparam('bookid', type_=Integer)
                )
            with create_connection() as conn:
                
                conn.execute(statement, {'bookid': id})
            return {"message": "Book delete successfully"}
        except SQLAlchemyError as e:
            # Xử lý lỗi và trả về phản hồi
            error_message = str(e)
            return {"error": error_message}
    @staticmethod
    def update_books_info(id: int, book: BookInfo):
        try:
            statement = BookTable.update().where(
                    BookTable.bookid ==bindparam('b_bookid', type_=Integer)
                ).values(
                bookname=book.book_name,
                author=book.author,
                publishyear=book.publish_year
            )
            with create_connection() as conn:
                conn.execute(statement, {'b_bookid': id})
            return {"message": "Book update successfully"}
        except SQLAlchemyError as e:
            # Xử lý lỗi và trả về phản hồi
            error_message = str(e)
            return {"error": error_message}
    @staticmethod
    def query_books_info(book: BookInfo):
        try:
            conditions = []

            if book.book_name != "":
                conditions.append(BookTable.bookname == book.book_name)
            if book.author != "":
                conditions.append(BookTable.author == book.author)
            if book.publish_year != -1:
                conditions.append(BookTable.publishyear == book.publish_year)
            if conditions:
                statement = select(BookTable).where(and_(*conditions))

            with create_connection() as conn:
                result: Result = conn.execute(statement)
                rows = result.fetchall()
                
                # Convert rows to a list of dictionaries
                result_json = [dict(row) for row in rows]

            return {"result": result_json}
        except SQLAlchemyError as e:
            # Xử lý lỗi và trả về phản hồi
            error_message = str(e)
            return {"error": error_message}
        
    @staticmethod
    def history_of_books(book: BookInfo):
        pass

 