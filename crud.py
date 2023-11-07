from sqlalchemy.orm import Session

import models
import schemas


def get_name(db: Session, name: str):
    return db.query(models.Star_wars).filter(models.Star_wars.name == name).first()


def get_faction(db: Session, faction: str, skip: int = 0, limit: int = 10):
    return db.query(models.Star_wars).filter(models.Star_wars.faction == faction).offset(skip).limit(limit).all()


