from fastapi import APIRouter, HTTPException, Depends
import asyncio
from ctrl.book import DML
from pydantic import BaseModel
from schema import BookInfo
from sqlalchemy.orm import Session
from database import get_db
from exceptions import *
router = APIRouter()


@router.post("/add_book", tags = ["Book"])
async def add_book(book: BookInfo, db: Session = Depends(get_db)):
    result = DML.add_books(db, book)
    if "error" in result:
        if "not found" in result["error"]:
            raise NotFoundException(result["error"])
        else:
            raise HTTPException(status_code=400, detail=result["error"])
    else:
        # Nếu thành công, trả về một thông báo thành công
        return {"message": "Book added successfully"}

@router.put("/update_book_info", tags = ["Book"])
async def update_book_info(id:int, book: BookInfo, db: Session = Depends(get_db)):
    result = DML.update_books_info(db, id, book)
    if "error" in result:
        if "not found" in result["error"]:
            raise NotFoundException(result["error"])
        else:
            raise HTTPException(status_code=400, detail=result["error"])
    else:
        # Nếu thành công, trả về một thông báo thành công
        return {"message": "Book updated successfully"}

@router.delete("/delete_book", tags = ["Book"])
async def delete_book(id: int, db: Session = Depends(get_db)):
    result = DML.delete_books(db, id)
    if "error" in result:
        if "not found" in result["error"]:
            raise NotFoundException(result["error"])
        else:
            raise HTTPException(status_code=400, detail=result["error"])
    else:
        return {"message": "Book delete successfully"}



@router.post("/query_book_info", tags = ["Book"])
async def query_book_info(book: BookInfo, db: Session = Depends(get_db)):
    result = DML.query_books_info(db, book)
    if "error" in result:
        if "not found" in result["error"]:
            raise NotFoundException(result["error"])
        else:
            raise HTTPException(status_code=400, detail=result["error"])
    else:
        return result


@router.get("/query_all_book", tags = ["Book"])
async def query_all_book(db: Session = Depends(get_db)):
    result = DML.query_all_books(db)
    if "error" in result:
        if "not found" in result["error"]:
            raise NotFoundException(result["error"])
        else:
            raise HTTPException(status_code=400, detail=result["error"])
    else:
        return result