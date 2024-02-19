# main.py
from fastapi import FastAPI
from apis import book, users, renting, analyst
from exceptions import *
from fastapi.responses import JSONResponse
from gunicorn.app.base import BaseApplication

# class CustomGunicornApp(BaseApplication):
#     def __init__(self, app, options=None):
#         self.options = options or {}
#         self.application = app
#         super().__init__()

#     def load_config(self):
#         for key, value in self.options.items():
#             self.cfg.set(key, value)

#     def load(self):
#         return self.application



app = FastAPI()
# app.add_exception_handler()
# Include routers from different modules
@app.exception_handler(NotFoundException)

async def custom_exception_handler(request, exc: NotFoundException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

app.include_router(book.router)
app.include_router(users.router)
app.include_router(renting.router)
app.include_router(analyst.router)

