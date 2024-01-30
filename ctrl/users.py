from sqlalchemy import create_engine, select, bindparam
from setting_database.db.core.initializer import create_connection
from model import *
from typing import List, Any, Dict
from schema import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_, and_
from sqlalchemy.engine import Result

class DML:
    @staticmethod
    def add_users(user: UserInfo):
        try:
            statement_checkusername = select(UserTable).where(
                UserTable.username==bindparam('c_username', type_=String)
            )
            with create_connection() as conn:
                result = conn.execute(statement_checkusername, {"c_username": user.username})

                # Sử dụng fetchone() để kiểm tra xem có dữ liệu hay không
                existing_user = result.fetchone()

            if existing_user:
                return {"error": "Username already exists"}
            statement = UserTable.insert().values(
                name=user.name,
                username=user.username,
                password=user.password,
                status = False
            )
            with create_connection() as conn:
                conn.execute(statement)
            return {"message": "User register successfully"}
        except SQLAlchemyError as e:
            # Xử lý lỗi và trả về phản hồi
            error_message = str(e)
            return {"error": error_message}
    def login(user: UserLogin):
        try:

            statement = select(UserTable).where(and_(
                UserTable.username==bindparam('c_username', type_=String),
                UserTable.password==bindparam('c_password', type_=String)
            ))
            with create_connection() as conn:
                result = conn.execute(statement, {"c_username": user.username, "c_password": user.password})
                check = result.fetchone()
            if check:
                return {"message": "Login successfully"}
            else:
                return {"error": "Wrong username or password"}
        except SQLAlchemyError as e:
            # Xử lý lỗi và trả về phản hồi
            error_message = str(e)
            return {"error": error_message}