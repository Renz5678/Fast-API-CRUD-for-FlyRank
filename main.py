from fastapi import FastAPI, Response
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

@app.get("/", description="Get root endpoint")
def get_root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

@app.get("/health", description="Get API health status")
def get_health():
    return {"status": "ok"}

@app.get("/tasks", description="Get all tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", description="Get task by ID")
def get_task_by_id(task_id: int):
    task = next((task for task in tasks if task["id"] == task_id), None)

    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found!"}
        )
    
    return task

@app.post("/tasks", description="Create new task")
def add_new_task(title: str):
    if title == "":
        return JSONResponse(
            status_code=400,
            content={"error": "Missing title!"}
        )
    
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }
    tasks.append(new_task)

    return JSONResponse(
        status_code=201,
        content=new_task
    )   

@app.put("/tasks/{task_id}", description="Update task")
def update_task(task_id: int, title: str, done: bool):
    task = next((task for task in tasks if task["id"] == task_id), None)

    if title is None or done is None:
            return JSONResponse(
            status_code=400,
            content={"error": f"Empty request body!"}
        )

    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found!"}
        )
    
    task["title"] = title
    task["done"] =  done

    return JSONResponse(
        status_code=200,
        content=task
    )

@app.delete("/tasks/{task_id}", description="Delete task")
def delete_task(task_id: int):
    task = next((task for task in tasks if task["id"] == task_id), None)

    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {task_id} not found!"}
        )
    
    tasks.remove(task)

    return Response(
        status_code=204
    )