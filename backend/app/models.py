from sqlalchemy import Column, Integer, String, Float, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer)
    hashed_password = Column(String)
    interests = Column(ARRAY(String))

class Ad(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True, index=True)
    field = Column(String, index=True)
    advertiser = Column(String, index=True)
    name = Column(String)
    description = Column(String)
    image_url = Column(String)
    ad_url = Column(String)
    target_audience = Column(String)
    bid = Column(Float)