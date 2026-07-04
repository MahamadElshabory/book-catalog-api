from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from contextlib import asynccontextmanager
from src.db.mainn import init_db

print("MAIN FILE LOADED 🚀")

@asynccontextmanager
async def life_span(app:FastAPI):
    print(f"server running ...")
    await init_db()
    yield
    print(f"server stopped ...")


version = "v1"

app = FastAPI(
    title="bookly",
    description="testing new",
    version = version,
    lifespan= life_span
)

app.include_router(book_router, prefix=f"/api/{version}/books")  # FOR BOOK

app.include_router(auth_router, prefix=f"/api/{version}/auth")  # FOR AUTH