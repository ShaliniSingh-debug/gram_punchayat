
import os
from fastapi import FastAPI, HTTPException, APIRouter, Depends, Request, Cookie
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import engine,get_db
from .. import schemas , models
from typing import List
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from ..config import settings
from datetime import datetime, timedelta, timezone
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.templating import Jinja2Templates

#secreset key
SECRETE_KEY = settings.secret_key
Algorithm = "HS256"
access_token_expire_minutes = 30


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMPLATE_DIR = os.path.join(BASE_DIR, "frontend", "templates")

templates = Jinja2Templates(directory=TEMPLATE_DIR)
router = APIRouter()

#hashing password
pwd_context = CryptContext(schemes=["bcrypt"] , deprecated= "auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def generate_token(data:dict):
              to_encode=data.copy()
              expire_time = datetime.now(timezone.utc)+ timedelta(minutes= access_token_expire_minutes)
              to_encode.update({"exp": expire_time})
              encode_jwt=jwt.encode(to_encode, SECRETE_KEY, algorithm= Algorithm)
              return encode_jwt

@router.get("/login" , response_class=HTMLResponse)


def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
#login method

@router.post("/login", response_class=HTMLResponse)

def login(request:OAuth2PasswordRequestForm=Depends(), db:Session = Depends(get_db)):
              get_user = db.query(models.User).filter(models.User.username == request.username).first()
              if not get_user: 
                            raise HTTPException(status_code = 404, detail="Invalid Credentials")
              if not pwd_context.verify(request.password,get_user.password):
                            raise HTTPException(status_code = 404 , detail = " Invalid Crdentails")
              access_token = generate_token(
                            data = {"sub":get_user.username}
              )
              response = RedirectResponse(url="/dashboard", status_code=302)
              response.set_cookie(key="access_token", value=access_token, httponly=True)
              return response


def get_current_user(access_token: str = Cookie(None), db: Session = Depends(get_db)):
              if not access_token:
                            raise HTTPException(status_code=401, detail="Not authenticated")
              cred_exception = HTTPException(status_code=401,
                                             detail="Invalid Auth Credentials",
                                             headers={'WWW-Authenticate' : "Bearer"})
              try:
                            payload = jwt.decode(access_token , SECRETE_KEY , algorithms=[Algorithm])
                            username : str = payload.get('sub')
                            if username is None:
                                          raise cred_exception
                            user = db.query(models.User).filter(models.User.username == username).first()
                            if not user:
                                          raise cred_exception
                            return user
                            # token_data = schemas.TokenData(email=useremail)
              except JWTError:
                            raise cred_exception

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, current_user: models.User = Depends(get_current_user)):
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "username": current_user.username,
            "email": current_user.email
        }
    )





              