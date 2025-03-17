
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI, Request,HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



DATABASE_URL = "postgresql://postgres:12345@localhost:5432/student"

# Create engine
engine = create_engine(DATABASE_URL)

# Create a session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

main_app = FastAPI(
    title="Student Management System",
    version="0.0.1",
    docs_url="/docs",  # Enable Swagger UI
    redoc_url="/redoc",  # Enable ReDoc UI
    openapi_url="/openapi.json"  # Enable OpenAPI JSON
)

origins = ["*"]

# Middleware configuration
main_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   

# main_app.mount("/api",main_app)

# Dependency for DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()