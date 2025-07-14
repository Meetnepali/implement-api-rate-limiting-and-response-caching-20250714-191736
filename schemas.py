from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

class CommentBase(BaseModel):
    username: str = Field(..., example="johndoe")
    content: str = Field(..., min_length=1, max_length=500, example="Great article!")

class CommentCreate(CommentBase):
    pass

class CommentResponse(CommentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class ErrorResponse(BaseModel):
    detail: str = Field(..., example="Article not found.")
