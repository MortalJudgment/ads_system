from sqlalchemy.orm import Session
from . import models, schemas
from typing import List
from .auth.authentication import get_password_hash

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(name=user.name, email=user.email, age=user.age, hashed_password=hashed_password, interests=user.interests)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_interests(db: Session, user_id: int, new_interests: List[str]):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.interests = new_interests
        db.commit()
        db.refresh(user)
    return user

def get_ads(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ad).offset(skip).limit(limit).all()

def create_ad(db: Session, ad: schemas.AdCreate):
    db_ad = models.Ad(**ad.dict())
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad