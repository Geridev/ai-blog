from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/article/", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db=db, article=article)

@app.get("/article/", response_model=list[schemas.Article])
def read_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    articles = crud.get_articles(db=db, limit=limit, skip=skip)
    return articles

@app.get("/article/{id}", response_model=schemas.Article)
def read_article(id: int, db: Session = Depends(get_db)):
    db_article = crud.get_article(id=id, db=db)
    if db_article is None:
        raise HTTPException(status_code=404, detail="Article nem talált")
    return db_article

@app.delete("/article/{id}", response_model=schemas.Article)
def remove_article(id: int, db: Session = Depends(get_db)):
    crud.delete_article(id=id, db=db)
    return "db_article"
