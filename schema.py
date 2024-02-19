from pydantic import BaseModel
import datetime
from typing import Optional
class BookInfo(BaseModel):
    bookname: str
    author: str
    publishyear: int
    category: str
class UserInfo(BaseModel):
    username: Optional[str]
    dateofbirth: Optional[datetime.date]


class RentInfo(BaseModel):
    userid: int
    bookid: int
    # dayofrent: date
    expirationdate: datetime.date


