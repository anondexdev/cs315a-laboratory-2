from fastapi import FastAPI, Query, Path

tasks_db: list[str] = ["Setup environment", "Write unit tests", "Deploy application"]

app = FastAPI()

@app.get("/tasks")
async def get_tasks():
   return {"tasks": len(tasks_db)}

@app.post("/tasks")
async def add_task(task_name: str = Query(min_length=3, max_length=50)):
   tasks_db.append(task_name)
   return {"message": "Task added successfully", "task_name":(tasks_db)}

@app.delete("/tasks/{task_index}")
async def delete_task(task_index: int = Path(ge=0)):
   if task_index < len(tasks_db):
       del tasks_db[task_index]
       return {"message": "Task removed", "deleted": task_index}
   else:
      return{"error":"Index out of range"}

inventory_db: dict[int, str] = {
   501: "Mechanical Keyboard",
   502: "Ergonomic Mouse",
   503: "USB-C Hub"
}

@app.get("/inventory")
async  def get_inventory():
   return {"inventory": inventory_db}

@app.get("/inventory/{item_id}")
async def get_item(item_id: int = Path(None, gt=0)):
   if item_id in inventory_db:
      return {"item_id": item_id, "item_name": inventory_db[item_id]}
   else:
      return {"error": "Item not found"}

@app.post("/inventory/{item_id}")
async def add_item(item_id: int = Path(gt=0), item_name: str = Query(min_length=2, max_length=30)):
    if item_id not in inventory_db:
        inventory_db[item_id] = item_name
        return {"message": "Item added successfully", "item_id": item_id, "item_name": item_name}

@app.delete("/inventory/{item_id}")
async def delete_item(item_id: int = Path(gt=0)):
    if item_id in inventory_db:
        del inventory_db[item_id]
        return {"message": "Item deleted successfully", "item_id": item_id}