from pydantic import BaseModel
class BookInfo(BaseModel):
    book_name: str
    author: str
    publish_year: int
class UserInfo(BaseModel):
    name: str
    username: str
    password: str
    # status: bool

class UserLogin(BaseModel):
    username: str
    password: str
