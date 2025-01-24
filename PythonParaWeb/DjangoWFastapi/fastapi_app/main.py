from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List

# Crear la instancia de FastAPI
app = FastAPI()

# Base para SQLAlchemy
Base = declarative_base()

# URL de conexión a la base de datos
DATABASE_URL = "postgresql://postgres:Santi_Aleja@localhost/user_db"

# Crear motor de SQLAlchemy
engine = create_engine(DATABASE_URL)

# Crear la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class User(Base):
    __tablename__ = 'usersmanage_user' #Nombre de la tabla de sql
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String)

class UserResponse(BaseModel):
    name: str
    email: str
    password: str

@app.get("/user/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    return user