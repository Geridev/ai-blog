from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from .database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String, unique=True, index=True)
    created = Column(DateTime, nullable=False, server_default=func.now())
    content = Column(String, nullable=False)
    views = Column(Integer, default=0)