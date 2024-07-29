from sqlalchemy.orm import Session
from app import models, schemas
from typing import List, Optional
import bcrypt

def get_user(db: Session, user_id: int) -> Optional[models.User]:
    """
    Retrieve a user by their ID.
    
    :param db: SQLAlchemy session
    :param user_id: User ID
    :return: User object or None
    """
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
    """
    Retrieve a user by their email.
    
    :param db: SQLAlchemy session
    :param email: User email
    :return: User object or None
    """
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    """
    Create a new user.
    
    :param db: SQLAlchemy session
    :param user: User creation schema
    :return: Created user object
    """
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.User(
        name=user.name,
        email=user.email,
        age=user.age,
        hashed_password=hashed_password,
        interests=user.interests
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_interests(db: Session, user_id: int, new_interests: List[str]) -> Optional[models.User]:
    """
    Update user interests.
    
    :param db: SQLAlchemy session
    :param user_id: User ID
    :param new_interests: List of new interests
    :return: Updated user object or None
    """
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.interests = new_interests
        db.commit()
        db.refresh(user)
    return user

def get_ads(db: Session, skip: int = 0, limit: int = 100) -> List[models.Ad]:
    """
    Retrieve ads with pagination.
    
    :param db: SQLAlchemy session
    :param skip: Number of records to skip
    :param limit: Maximum number of records to return
    :return: List of ads
    """
    return db.query(models.Ad).offset(skip).limit(limit).all()

def create_ad(db: Session, ad: schemas.AdCreate) -> models.Ad:
    """
    Create a new ad.
    
    :param db: SQLAlchemy session
    :param ad: Ad creation schema
    :return: Created ad object
    """
    db_ad = models.Ad(**ad.dict())
    db.add(db_ad)
    db.commit()
    db.refresh(db_ad)
    return db_ad

def get_ads_by_interests(db: Session, interests: List[str], limit: int = 10) -> List[models.Ad]:
    """
    Retrieve ads by interests.
    
    :param db: SQLAlchemy session
    :param interests: List of interests
    :param limit: Maximum number of records to return
    :return: List of ads
    """
    return db.query(models.Ad).filter(models.Ad.field.in_(interests)).order_by(models.Ad.bid.desc()).limit(limit).all()

def search_ads(db: Session, keywords: List[str], limit: int = 5) -> List[models.Ad]:
    """
    Search ads by keywords.
    
    :param db: SQLAlchemy session
    :param keywords: List of keywords
    :param limit: Maximum number of records to return
    :return: List of ads
    """
    query = db.query(models.Ad)
    for keyword in keywords:
        query = query.filter(
            models.Ad.description.ilike(f"%{keyword}%") |
            models.Ad.name.ilike(f"%{keyword}%") |
            models.Ad.field.ilike(f"%{keyword}%")
        )
    return query.order_by(models.Ad.bid.desc()).limit(limit).all()