# main.py
from fastapi import FastAPI
from apis import book, users

app = FastAPI()

# Include routers from different modules
app.include_router(book.router)
app.include_router(users.router)
