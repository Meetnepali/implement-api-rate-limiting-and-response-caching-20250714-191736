from fastapi import FastAPI
from routers.comments import router as comments_router
from routers.notifications import router as notifications_router
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db import Base
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./test.db")

enable_docs = True  # Set False if OpenAPI docs should be hidden

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # For SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI(openapi_url="/openapi.json" if enable_docs else None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# Routers
app.include_router(comments_router, prefix="/articles", tags=["Comments"])
app.include_router(notifications_router, prefix="/notifications", tags=["Notifications"])
