import openai
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session

from . import models, schemas 

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_article(db: Session, id: int):
    return db.query(models.Article).filter(models.Article.id == id).first()

def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Article).offset(skip).limit(limit).all()

def create_article(db: Session, article: schemas.ArticleCreate):
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": article.prompt}]
    )
    db_article = models.Article(prompt = article.prompt, content = chat_completion.choices[0].message.content)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def delete_article(db: Session, id: int):
    db_article = db.query(models.Article).filter(models.Article.id == id).first()
    db.delete(db_article)
    db.commit()
    return "Sikeres törlés"
