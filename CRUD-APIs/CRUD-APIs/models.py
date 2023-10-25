from sqlalchemy import Column, String, Integer, Boolean
from .database import Base,engine 




class Users(Base):               #model
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index= True)
    email = Column(String,unique=True, index = True)
    is_active = Column(Boolean,default=True )


Base.metadata.create_all(bind=engine)   #this will convert the models to tables in the DB      