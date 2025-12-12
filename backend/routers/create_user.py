import os
from fastapi import FastAPI, HTTPException, APIRouter, Depends,Request, Form
from sqlalchemy.orm import Session
from ..database import engine,get_db
from .. import schemas , models
from typing import List
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMPLATE_DIR = os.path.join(BASE_DIR, "frontend", "templates")

templates = Jinja2Templates(directory=TEMPLATE_DIR)
router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"] , deprecated= "auto")


@router.post("/users", response_model=schemas.DisplayUser , response_class=HTMLResponse)

def create_user(request : Request ,
                username : str = Form(...),
                password : str = Form(...),
                email: str = Form(...),
                first_name: str = Form(...),
                last_name: str = Form(...),
                db: Session= Depends(get_db)
                ):
              hashed_password = pwd_context.hash(password)
              
              
              #check if email exists in the db 
              existing_emai = db.query(models.User).filter(models.User.email ==email).first()
              

              if existing_emai:
                            return templates.TemplateResponse(
                            "create_user.html",
                            {"request": request, "error": "Email already exists!"}
                            )
              
              #check if username exits already in database
              existing_user = db.query(models.User).filter(models.User.username == username).first()
              if existing_user:
                            return templates.TemplateResponse("create_user.html",
                                          {"request":request , "error": "The username already Exits, Choose different username"})
              
              
                           
              new_user= models.User(username = username , password = hashed_password ,
                                          email = email , first_name = first_name , last_name = last_name)
              db.add(new_user)
              db.commit()
              db.refresh(new_user)
              return templates.TemplateResponse(
                              "create_user.html",
                              {
                                  "request": request,
                                  "success": "User created successfully!",
                                  "show_login_button": True
                              }
                          )

@router.get("/users", response_class=HTMLResponse)
def create_users_page(request: Request):
              return templates.TemplateResponse("create_user.html", {"request": request})

              