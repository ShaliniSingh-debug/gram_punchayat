
from fastapi import FastAPI, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import engine,get_db
from .. import schemas , models
from typing import List

router = APIRouter()

@router.post("/users", response_model=schemas.DisplayUser)

def create_user(db: Session= Depends(get_db)):
              pass
              