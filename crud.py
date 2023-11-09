from sqlalchemy.orm import Session

import models
import schemas


def get_name(db: Session, name: str):
    return db.query(models.Star_wars).filter(models.Star_wars.name == name).first()


def get_faction(db: Session, faction: str, skip: int = 0, limit: int = 10):
    return db.query(models.Star_wars).filter(models.Star_wars.faction == faction).offset(skip).limit(limit).all()

def create_character(db: Session, user: schemas.star_wars_create):
    db_star_Wars = models.Star_wars(**user.dict())
    db.add(db_star_Wars)
    db.commit()
    db.refresh(db_star_Wars)
    return db_star_Wars