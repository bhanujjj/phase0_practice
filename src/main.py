from fastapi import FastAPI
from src.db import engine
from src.models import Base
from src.routers import users

app = FastAPI(title="ML Template API")

# include routes
app.include_router(users.router)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
