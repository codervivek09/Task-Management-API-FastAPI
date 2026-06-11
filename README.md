# Task-Management-API-FastAPI

# Task Management API

A RESTful Task Management API built using FastAPI, MySQL, SQLAlchemy, and JWT Authentication. This application allows users to register, log in securely, and manage tasks through protected CRUD APIs.

## Features

* User Registration
* Secure Login with JWT Authentication
* Password Hashing using bcrypt
* Create Tasks
* View Tasks
* Update Tasks
* Delete Tasks
* Protected Routes using OAuth2 and JWT
* MySQL Database Integration
* Swagger API Documentation

## Tech Stack

* Python
* FastAPI
* MySQL
* SQLAlchemy
* Pydantic
* JWT (JSON Web Tokens)
* OAuth2
* Passlib (bcrypt)
* Uvicorn
* Git & GitHub

## Project Structure

```text
Task-Management-API/
│
├── app/
│   ├── auth.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   │
│   └── routes/
│       ├── user.py
│       └── task.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/codervivek09/Task-Management-API-FastAPI.git
cd Task-Management-API-FastAPI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure MySQL

Create a database:

```sql
CREATE DATABASE taskdb;
```

Update database credentials in `app/database.py`.

### Run Application

```bash
python -m uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Authentication

| Method | Endpoint  | Description                  |
| ------ | --------- | ---------------------------- |
| POST   | /register | Register a new user          |
| POST   | /login    | Login and generate JWT token |

### Tasks

| Method | Endpoint         | Description   |
| ------ | ---------------- | ------------- |
| POST   | /tasks           | Create a task |
| GET    | /tasks           | Get all tasks |
| PUT    | /tasks/{task_id} | Update a task |
| DELETE | /tasks/{task_id} | Delete a task |

## Authentication Flow

1. Register a user.
2. Login using email and password.
3. Receive JWT access token.
4. Click **Authorize** in Swagger UI.
5. Access protected task APIs.

## Sample Task Request

```json
{
  "title": "Learn JWT",
  "description": "Implement authentication in FastAPI"
}
```

## Future Enhancements

* User-specific tasks
* Task priorities
* Due dates
* Task filtering and search
* Pagination
* Cloud deployment

## Author

**Vivek Phad**

Electronics & Telecommunication Student

Python | FastAPI | SQL | Backend Development

GitHub: https://github.com/codervivek09
