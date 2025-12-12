from pydantic import BaseModel,EmailStr
from typing import Optional

class UserDetails(BaseModel):
              username : str
              email : EmailStr
              password : str
              first_name : str
              last_name : str

class DisplayUser(BaseModel):
              first_name:str
              last_name:str
              email:EmailStr
              class Config:
                            orm_mode = True