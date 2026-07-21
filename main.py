from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

tasks = [
    {
        "id": 1,
        "title": "Household chores",
        "done": True
    }, 
    {
        "id": 2,
        "title": "Internship Tasks",
        "done": False
    }, 
    {
        "id": 3,
        "title": "Freelance Website",
        "done": False
    }, 
]

@app.get("/")
def get_root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/health")
def get_health():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{item_id}")
def get_task_by_id(item_id: int):
    task = next((task for task in tasks if task["id"] == item_id), None)

    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {item_id} not found"}
        )
    
    return task