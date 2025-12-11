from fastapi import FastAPI
from contextlib import asynccontextmanager
from . import models
from .database import engine


models.Base.metadata.create_all(engine)
# # def create_db_and_tables():
# #     models.Base.metadata.create_all(bind=engine)

    
# app = FastAPI()

# # @asynccontextmanager
# # async def lifespan(app: FastAPI):
# #     create_db_and_tables()
# #     yield

app = FastAPI()

