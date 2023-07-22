from pydantic import BaseModel
from datetime import datetime

class ArticleBase(BaseModel):
    prompt: str

class ArticleCreate(ArticleBase):
    prompt: str

class Article(ArticleBase):
    id: int
    created: datetime
    views: int
    content: str

    class Config:
        orm_mode = True