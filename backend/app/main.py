from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi.staticfiles import StaticFiles
from typing import List
from . import crud, models, schemas
from .database import engine, SessionLocal
from .auth import authentication
from database.db_connection import get_db
from database import db_queries

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Include authentication router
app.include_router(authentication.router, prefix="/auth", tags=["auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Ads System API"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db_queries.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return db_queries.create_user(db=db, user=user)

@app.put("/users/{user_id}/interests", response_model=schemas.User)
def update_user_interests(user_id: int, interests: List[str], db: Session = Depends(get_db)):
    updated_user = crud.update_user_interests(db, user_id, interests)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.get("/ads/", response_model=List[schemas.Ad])
def read_ads(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ads = db_queries.get_ads(db, skip=skip, limit=limit)
    return ads
# Add more endpoints as needed