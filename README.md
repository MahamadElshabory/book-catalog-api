# Book Catalog API

A REST API for managing a book catalog with user authentication and asynchronous background jobs, built to practice production backend patterns: JWT auth, async task queues, and relational data modeling.

# Features
Full CRUD for books (create, read, update, delete)
JWT-based authentication and authorization
Background email sending via Celery + Redis (non-blocking request handling)
PostgreSQL persistence with SQLModel ORM
Auto-generated API docs (OpenAPI/Swagger via FastAPI)

# Tech Stack

FastAPI PostgreSQL SQLModel Celery Redis JWT Docker

# Architecture

Requests hit FastAPI route handlers, which validate input via Pydantic/SQLModel schemas and write to PostgreSQL. Any slow operation — currently email notifications on book events — is offloaded to a Celery worker via a Redis broker, so the API response isn't blocked waiting on I/O. This mirrors the pattern used for real async workloads like notification systems or report generation.

# What I focused on

This project was where I learned how to decouple request/response cycles from slow side-effects using a task queue — a pattern that shows up constantly in production backends (emails, PDF generation, ML inference, etc.), not just this one use case.

# Run locally

bash
docker-compose up --build

API docs available at /docs.

# Possible next steps
Add pytest test suite
Add rate limiting
Deploy live demo (Render/Railway)
