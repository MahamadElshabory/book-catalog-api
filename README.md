# Bookly FastAPI Project

Bookly is a backend API project built with FastAPI. It includes a Books CRUD module, user authentication, PostgreSQL database integration, JWT authentication, and background email sending using Celery and Redis.

## Features

- Books CRUD module with separate routes, schemas, models, and service layer
- Create, read, update, and delete book records
- User signup and login
- Password hashing
- JWT token generation
- PostgreSQL database integration
- SQLModel ORM
- Async database sessions
- Celery background tasks
- Redis message broker
- Email sending after signup
- Environment-based configuration


## Project Structure

```txt
src/
├── auth/
│   ├── models.py
│   ├── routes.py
│   ├── schema.py
│   ├── service.py
│   └── utils.py
│
├── books/
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   └── service.py
│
├── db/
│   └── mainn.py
│
├── celery_tasks.py
├── mail.py
├── configg.py
└── main.py

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLModel
- SQLAlchemy Async
- Pydantic
- Celery
- Redis
- FastAPI-Mail
- JWT
- Docker

## Project Flow

When a user signs up:

1. FastAPI receives the signup request.
2. The user is saved in PostgreSQL.
3. FastAPI sends an email task to Celery.
4. Redis stores the background task.
5. Celery worker receives the task.
6. The email is sent in the background.

## How to Run

### 1. Create virtual environment

```bash
python -m venv env