from fastapi import APIRouter, HTTPException
import asyncio
from pydantic import BaseModel
from schema import *
from ctrl.users import DML
router = APIRouter()



@router.post("/registering")
async def registering(user: UserInfo):
    result = DML.add_users(user)
    if "error" in result:
        # Nếu có lỗi, ném một HTTPException với mã lỗi 500 và thông báo lỗi
        raise HTTPException(status_code=500, detail=result["error"])
    else:
        # Nếu thành công, trả về một thông báo thành công
        return {"message": "User register successfully"}
    
@router.post("/login")
async def login(user:UserLogin):
    result = DML.login(user)
    if "error" in result:
        # Nếu có lỗi, ném một HTTPException với mã lỗi 500 và thông báo lỗi
        raise HTTPException(status_code=500, detail=result["error"])
    else:
        # Nếu thành công, trả về một thông báo thành công
        return {"message": "Login sucess"}    
