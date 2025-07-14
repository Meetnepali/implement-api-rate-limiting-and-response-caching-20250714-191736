from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, status
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from db import get_db
from routers.notifications import notify_author

router = APIRouter()

# GET /articles/{article_id}/comments/
@router.get("/{article_id}/comments/", response_model=List[schemas.CommentResponse], responses={404: {"model": schemas.ErrorResponse, "description": "Article not found."}})
def list_comments(article_id: int, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found.")
    comments = db.query(models.Comment).filter(models.Comment.article_id == article_id).order_by(models.Comment.created_at.desc()).all()
    return comments

# POST /articles/{article_id}/comments/
@router.post("/{article_id}/comments/", response_model=schemas.CommentResponse, status_code=201, responses={404: {"model": schemas.ErrorResponse, "description": "Article not found."},400: {"model": schemas.ErrorResponse, "description": "Invalid Input."}})
def create_comment(article_id: int, comment: schemas.CommentCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found.")
    db_comment = models.Comment(
        article_id=article_id,
        username=comment.username,
        content=comment.content
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)

    # Simulate real-time notification
    background_tasks.add_task(
        notify_author,
        article_title=article.title,
        author_email=article.author_email,
        comment_username=comment.username,
        comment_content=comment.content
    )

    return db_comment
