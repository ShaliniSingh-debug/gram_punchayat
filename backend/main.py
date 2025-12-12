from fastapi import FastAPI
from contextlib import asynccontextmanager
from . import models, schemas
from .database import engine
from .routers import create_user , login, dashboard


models.Base.metadata.create_all(engine)
# # def create_db_and_tables():
# #     models.Base.metadata.create_all(bind=engine)

    
# app = FastAPI()

# # @asynccontextmanager
# # async def lifespan(app: FastAPI):
# #     create_db_and_tables()
# #     yield

app = FastAPI()
app.include_router(create_user.router)

app.include_router(login.router)
# app.include_router(dashboard.router)

