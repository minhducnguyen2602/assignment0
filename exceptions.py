# exceptions.py

from fastapi import HTTPException, status

class NotFoundException(HTTPException):
    def __init__(self, detail: str, status_code: int = status.HTTP_404_NOT_FOUND):
        super().__init__(status_code=status_code, detail=detail)
