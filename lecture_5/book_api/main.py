from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import or_

# Import local files
import models
import schemas
from database import SessionLocal, engine

# Create tables in DB
models.Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI()

# Create Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create book
@app.post("/books/",response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        year=book.year
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Book search
@app.get("/books/search/",response_model=List[schemas.Book]) # Вот здесь выдает неверный ответ
def search_books(
        title: str | None = None,
        author: str | None = None,
        year: int | None = None,
        db: Session = Depends(get_db)
):
    query = db.query(models.Book)

    conditions = []
    if title:
        conditions.append(models.Book.title.ilike(f"%{title}%"))
    if author:
        conditions.append(models.Book.author.ilike(f"%{author}%"))
    if year:
        conditions.append(models.Book.year == year)

    if conditions:
        query = query.filter(or_(*conditions))

    books = query.all()

    if not books:
        raise HTTPException(status_code=404, detail="Books not found")

    return books

# Get book
@app.get("/books/{book_id}",response_model=schemas.Book)
def read_book(book_id : int, db : Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return db_book

# Update book
@app.put("/books/{book_id}",response_model=schemas.Book)
def update_book(book_id : int, book_update : schemas.BookCreate, db : Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db_book.title = book_update.title
    db_book.author = book_update.author
    db_book.year = book_update.year

    db.commit()
    db.refresh(db_book)
    return db_book

# Delete book
@app.delete("/books/{book_id}")
def delete_book(book_id : int, db : Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted"}




