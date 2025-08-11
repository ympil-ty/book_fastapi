import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Как хорошо лежать на кровати",
        "author": "Пупа",
    },
    {
        "id": 2,
        "title": "Как хорошо лежать на пляже",
        "author": "Лупа",
    }
]

@app.get(
    "/books",
    tags=["Книги"],
    summary="Получить все книги"
)
def show_books():
    return books


@app.get(
    "/books/{id}",
    tags=["Книги"],
    summary="Получить книгу по ID"
)
def get_book(id: int):
    for book in books:
        if book["id"] == id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")


class NewBook(BaseModel):
    title: str
    author: str


@app.post("/books",
          tags=["Книги"],
          summary="Добавить книгу"
)
def book_add(new_book: NewBook):
    books. append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author,
    })
    return {"success": True, "message": "Книга добавлена"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

