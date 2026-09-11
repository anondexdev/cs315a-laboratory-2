from fastapi import FastAPI

app = FastAPI()

student_list = ["Uno", "Dos", "Trev", "Micah"]


@app.get("/student/{student_id}")
async def get_student(student_id: int):
  return {"message": student_list[student_id]}

@app.post('/student/{student_id}')
async def add_student(student_name: str):

  student_list.append(student_name)
  return {"message" : "Student added successfully"}

@app.put('/student/{student_id}')
async def update_student(student_id: int, student_name: str):
  student_list[student_id] = student_name
  return {"message" : "Student updated successfully"}

@app.delete("/student/{student_id}")
async def delete_student(student_id: int):
  del student_list[student_id]
  return {"message" : "Student deleted successfully"}


