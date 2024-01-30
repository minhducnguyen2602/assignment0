from fastapi import APIRouter, HTTPException
import asyncio
from ctrl.book import DML
from pydantic import BaseModel
from schema import BookInfo

router = APIRouter()


@router.post("/add_book")
async def add_book(book: BookInfo):
    result = DML.add_books(book)
    if "error" in result:
        # Nếu có lỗi, ném một HTTPException với mã lỗi 500 và thông báo lỗi
        raise HTTPException(status_code=500, detail=result["error"])
    else:
        # Nếu thành công, trả về một thông báo thành công
        return {"message": "Book added successfully"}

@router.put("/update_book_info")
async def update_book_info(id:int, book: BookInfo):
    result = DML.update_books_info(id, book)
    if "error" in result:
        # Nếu có lỗi, ném một HTTPException với mã lỗi 500 và thông báo lỗi
        raise HTTPException(status_code=500, detail=result["error"])
    else:
        # Nếu thành công, trả về một thông báo thành công
        return {"message": "Book added successfully"}

@router.delete("/delete_book")
async def delete_book(id: int):
    result = DML.delete_books(id)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    else:
        return {"message": "Book delete successfully"}



@router.post("/query_book_info")
async def query_book_info(book: BookInfo):
    result = DML.query_books_info(book)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    else:
        return result


@router.get("/history_of_book")
async def rental_history_of_book(id: int):
    DML.history_of_books()