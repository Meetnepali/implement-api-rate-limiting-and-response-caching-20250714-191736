from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from db import Base

# Assume Article table/model is present
class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey('articles.id'), nullable=False)
    username = Column(String(64), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    article = relationship('Article', back_populates='comments')

# For demonstration: add relationship to Article
# The Article model is assumed to exist elsewhere with the following minimal structure
# class Article(Base):
#     __tablename__ = 'articles'
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(256), nullable=False)
#     author_email = Column(String(128), nullable=False)
#     comments = relationship('Comment', back_populates='article')
