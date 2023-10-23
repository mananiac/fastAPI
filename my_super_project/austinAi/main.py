from fastapi import FastAPI,Depends, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from pydantic import BaseModel      #used for schema
from sqlalchemy.orm import Session

from .database import Base,engine,SessionLocal 
from .models import Users

app = FastAPI()

class UserSchema(BaseModel):    #schema
     id : int
     email: str
     is_active: bool

     class Config:
         orm_mode = True

def get_db():               # Dependency
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return "go to /docs"

@app.get("/users", response_model=List[UserSchema])
def get_users(db:Session = Depends(get_db)):
    return db.query(Users).all()

@app.post("/users", response_model=UserSchema)
def create_user(newUser : UserSchema, db:Session = Depends(get_db)):
     UserObj = Users(id = newUser.id, email = newUser.email, is_active = newUser.is_active)
     db.add(UserObj)
     db.commit()
     return UserObj

@app.put("/users/{user_id}", response_model=UserSchema)
def update_user(user_id : int, newUser : UserSchema, db:Session = Depends(get_db)):
    try:
        UserObj=db.query(Users).filter(Users.id ==user_id).first()
        UserObj.email=newUser.email
        UserObj.is_active=newUser.is_active
        db.add(UserObj)
        db.commit()
        return UserObj 
    except:
        return HTTPException(status_code=404,detail="user not found")
    
@app.delete("/users/{user_id}", response_class=JSONResponse)
def delete_user(user_id : int, db:Session = Depends(get_db)):
    try:
        UserObj=db.query(Users).filter(Users.id ==user_id).first()
        db.delete(UserObj)
        db.commit()
        return "deleted"
    except:
        return HTTPException(status_code=404,detail="user not found")    
    

