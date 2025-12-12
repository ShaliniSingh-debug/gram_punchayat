# import os
# from backend.routers.login import get_current_user
# from fastapi import FastAPI, HTTPException, APIRouter, Depends, Request
# from fastapi.security.oauth2 import OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session
# from ..database import engine,get_db
# from .. import schemas , models
# from typing import List
# from passlib.context import CryptContext
# from jose import JWTError, jwt
# from fastapi.security import OAuth2PasswordBearer
# from ..config import settings
# from datetime import datetime, timedelta, timezone
# from fastapi.responses import HTMLResponse,RedirectResponse
# from fastapi.templating import Jinja2Templates


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# TEMPLATE_DIR = os.path.join(BASE_DIR, "frontend", "templates")

# templates = Jinja2Templates(directory=TEMPLATE_DIR)
# router = APIRouter()
# @router.get("/dashboard" , response_class=HTMLResponse)

# def dashboard(db:Session=Depends(get_db) , current_user :schemas.UserDetails = Depends(get_current_user)):
#               return current_user
              