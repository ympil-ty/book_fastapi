📚 FastAPI Book API

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green)
![GitHub last commit](https://img.shields.io/github/last-commit/ympil-ty/book_fastapi)

**REST API для управления коллекцией книг** с автоматической документацией (Swagger/OpenAPI).

🌟 Возможности
- `GET /books` — Получить список всех книг
- `GET /books/{id}` — Найти книгу по ID
- `POST /books` — Добавить новую книгу (название, автор)
- Автоматическая генерация ID для новых книг

🛠 Установка
1. Клонируйте репозиторий:
`git clone https://github.com/ympil-ty/book_fastapi.git
cd book_fastapi`
2. Установите зависимости:
`pip install fastapi uvicorn`
3. Запустите сервер:
`uvicorn main:app --reload`
📖 Документация API

После запуска откройте:

Swagger UI: (http://localhost:8000/docs) 
ReDoc: (http://localhost:8000/redoc) 

