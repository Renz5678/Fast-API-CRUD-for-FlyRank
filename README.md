# Task API 

A simple API built with FastAPI that demonstrates basic CRUD for tasks

---

## Features

- API information endpoint
- Health check endpoint
- Get all tasks
- Get a task by ID
- Create a new task
- Update a task
- Delete a task

---

## Prerequisites

- Python 3.10 or newer

--- 

## Installation:

### 1. Clone the repository


```bash
git clone https://github.com/Renz5678/Fast-API-CRUD-for-FlyRank.git
cd Fast-API-CRUD-for-FlyRank
```

### 2. Install dependencies (FastAPI)

```bash
pip install fastapi[standard]
```

### Run the API

```bash
fastapi dev main.py
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{task_id}` | Get a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

---

## Example Request

### Get all tasks

```bash
curl -i http://127.0.0.1:8000/tasks
```

Example output:

```http
HTTP/1.1 200 OK
content-type: application/json

[
  {
    "id": 1,
    "title": "Household chores",
    "done": true
  },
  {
    "id": 2,
    "title": "Internship Tasks",
    "done": false
  },
  {
    "id": 3,
    "title": "Freelance Website",
    "done": false
  }
]
```

## Swagger UI

API documentation automatically created by FastAPI

accessible through

```
http://127.0.0.1:8000/docs
```

### Screenshot
![Swagger UI](fastapi_screenshot.png)
