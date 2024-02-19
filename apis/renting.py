from fastapi import APIRouter, HTTPException, Depends
import asyncio
from ctrl.renting import DML
from pydantic import BaseModel
from schema import *
from sqlalchemy.orm import Session
from database import get_db
from exceptions import *
router = APIRouter()


@router.post("/rent_book", tags = ["Renting"])
async def add_rent(rent: RentInfo, db: Session = Depends(get_db)):
    result = DML.add_rents(db, rent)
    if "error" in result:
        if "not found" in result["error"]:
            raise NotFoundException(result["error"])
        else:
            raise HTTPException(status_code=400, detail=result["error"])
    else:
        # Nếu thành công, trả về một thông báo thành công
        return {"message": "Rent successfully"}


@router.post("/return_book", tags = ["Renting"])
async def return_rent(rentid: int, db: Session = Depends(get_db)):
    result = DML.return_rents(db, rentid)
    if "error" in result:
        # Nếu có lỗi, ném một HTTPException với mã lỗi 400 và thông báo lỗi
        raise HTTPException(status_code=400, detail=result["error"])
    else:
        # Nếu thành công, trả về một thông báo thành công
        return {"message": "Return successfully"}

