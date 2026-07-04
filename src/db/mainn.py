from sqlalchemy.ext.asyncio import create_async_engine
# from sqlalchemy.ext.asyncio import  AsyncEngine # create_async_engine
from sqlmodel import SQLModel
# from sqlmodel import create_engine , text
from src.books.models import Book
from src.configg import Config
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession


# Create async engine
engine = create_async_engine(
    Config.DATABASE_URL,
    echo=True
)


# Test database connection
async def init_db():
    print("INIT DB IS RUNNING 🔥")
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
        
        
        

async def get_session() -> AsyncSession:
    Session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session
        
        

"""
async def get_session() -> AsyncSession:
    Session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with Session() as session:
        yield session        
        
        """