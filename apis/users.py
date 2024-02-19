from fastapi import APIRouter, HTTPException, Depends
import asyncio
from pydantic import BaseModel
from schema import *
from ctrl.users import DML
from sqlalchemy.orm import Session
from database import get_db
from exceptions import *
router = APIRouter()



@router.post("/registering", tags = ["User"])
async def registering(user: UserInfo, db: Session = Depends(get_db)):
    result = DML.add_users(db, user)
    if "error" in result:
        if "not found" in result["error"]:
            raise NotFoundException(result["error"])
        else:
            raise HTTPException(status_code=400, detail=result["error"])
    else:
        # Nếu thành công, trả về một thông báo thành công
        return {"message": "User register successfully"}
    
    


@router.put("/update_user_information", tags = ["User"])
async def update_user(id: int, user: UserInfo, db: Session = Depends(get_db)):
    result = DML.update_users(id, db, user)
    if "error" in result:
        if "not found" in result["error"]:
            raise NotFoundException(result["error"])
        else:
            raise HTTPException(status_code=400, detail=result["error"])
    else:
        # Nếu thành công, trả về một thông báo thành công
        return {"message": "User update successfully"}
