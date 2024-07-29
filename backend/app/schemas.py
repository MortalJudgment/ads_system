from pydantic import BaseModel, EmailStr
from typing import List, Optional

class InterestBase(BaseModel):
    name: str

class InterestCreate(InterestBase):
    pass

class Interest(InterestBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserCreate(UserBase):
    password: str
    interests: List[str]

class User(UserBase):
    id: int
    interests: List[Interest]

    class Config:
        orm_mode = True

class AdBase(BaseModel):
    field: str
    advertiser: str
    name: str
    description: str
    image_url: str
    ad_url: str
    target_audience: str
    bid: float

class AdCreate(AdBase):
    pass

class Ad(AdBase):
    id: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None