# Book Catalog API
## Overview

This is a REST API for managing a book catalog, built to practice patterns that show up constantly in real production backends: authenticated APIs, relational data modeling, and background job processing that doesn't block the main request cycle.

The core problem this project solves is a common one — some operations (like sending a confirmation email after a book is added) are too slow to run inside a normal HTTP request without hurting response times. Instead of making the user wait, those operations are handed off to a background worker so the API responds immediately while the slower work happens asynchronously. This is the same pattern used in production systems for things like sending notifications, generating reports, or processing uploads — the book catalog is just the concrete use case I used to implement and understand it properly.

I built this to go deeper into FastAPI beyond basic CRUD: adding real authentication, a proper ORM layer with SQLModel, and a task queue with Celery and Redis, all wired together and containerized with Docker so it runs the same way anywhere.



## Features
Full CRUD for books (create, read, update, delete)
JWT-based authentication and authorization
Background email sending via Celery + Redis (non-blocking request handling)
PostgreSQL persistence with SQLModel ORM
Auto-generated API docs (OpenAPI/Swagger via FastAPI)
Tech Stack

FastAPI PostgreSQL SQLModel Celery Redis JWT Docker


## Architecture
Client → FastAPI route → validate (SQLModel/Pydantic) → PostgreSQL
                              │
                              └──→ enqueue job → Redis → Celery worker → send email

The API layer and the background worker are decoupled through Redis as the message broker — the API never waits on the worker, and the worker can be scaled independently if job volume grows.


## Run locally
bash
docker-compose up --build

API docs available at /docs.

## Possible next steps
Add a pytest test suite
Add rate limiting
Deploy a live demo (Render/Railway)
