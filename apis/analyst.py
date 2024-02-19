from fastapi import APIRouter, HTTPException, Depends
import asyncio
from ctrl.analyst import DML
from pydantic import BaseModel
from schema import *
from sqlalchemy.orm import Session
from database import get_db
from exceptions import *
router = APIRouter()


@router.post("/query_rentalhistory_book", tags = ["Book"])
async def query_rentalhistory_book(bookid: int, db: Session = Depends(get_db)):
    result = DML.query_rentalhistory_books(db, bookid)
    if "error" in result:
        if "not found" in result["error"]:
            raise NotFoundException(result["error"])
        else:
            raise HTTPException(status_code=400, detail=result["error"])
    else:
        return result
    
@router.post("/query_rentalhistory_user", tags = ["User"])
async def query_rentalhistory_users(userid: int, db: Session = Depends(get_db)):
    result = DML.query_rentalhistory_users(db, userid)
    if "error" in result:
        if "not found" in result["error"]:
            raise NotFoundException(result["error"])
        else:
            raise HTTPException(status_code=400, detail=result["error"])
    else:
        return result
    
@router.get("/query_rental_of_category", tags = ["Renting"])
async def query_rentalofcategory(db: Session = Depends(get_db)):
    result = DML.query_rental_of_categories(db)
    if "error" in result:
        if "not found" in result["error"]:
            raise NotFoundException(result["error"])
        else:
            raise HTTPException(status_code=400, detail=result["error"])
    else:
        return result


