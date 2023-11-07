from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

# "sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/faction/Jedi", response_model=list[schemas.star_wars_base])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_faction(db, faction="Jedi", skip=skip, limit=limit)
    return users


@app.get("/faction/Sith", response_model=list[schemas.star_wars_base])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_faction(db, faction="Sith", skip=skip, limit=limit)
    return users


@app.get("/name/{user_id}", response_model=schemas.star_wars)
def read_user(name: str, db: Session = Depends(get_db)):
    db_user = crud.get_name(db, name=name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
