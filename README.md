# Bookly FastAPI Project

Bookly is a backend API project built with FastAPI. It includes book CRUD operations, user authentication, PostgreSQL database integration, JWT authentication, and background email sending using Celery and Redis.

## Features

- FastAPI backend
- PostgreSQL database
- SQLModel ORM
- Async database sessions
- Book CRUD APIs
- User signup and login
- Password hashing
- JWT token generation
- Celery background tasks
- Redis message broker
- Email sending after signup
- Environment-based configuration

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