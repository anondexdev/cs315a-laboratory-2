from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from db import engine, Model, get_db
import models
import schemas


Model.metadata.create_all(bind=engine)

app=FastAPI(title="Task_Manager_API")

@app.post(
    "/users/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED
)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.username == user.username).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Username already registered or existing",
        )
    new_user = models.User(username=user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
# ==========================================
# 2. CREATE TASK FOR USER ENDPOINT
# ==========================================
@app.post(
    "/users/{user_id}/tasks/",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task_for_user(
    user_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    owner = db.query(models.User).filter(models.User.id == user_id).first()
    if not owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    new_task = models.Task(
        title=task.title,
        description=getattr(task, "descript", None),
        owner_id=user_id,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from db import engine, Model, get_db
import models
import schemas

Model.metadata.create_all(bind=engine)

app=FastAPI(title="Task_Manager_API")

@app.post(
    "/users/", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED
)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.username == user.username).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Username already registered or existing",
        )
    new_user = models.User(username=user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
# ==========================================
# 2. CREATE TASK FOR USER ENDPOINT
# ==========================================
@app.post(
    "/users/{user_id}/tasks/",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task_for_user(
    user_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    owner = db.query(models.User).filter(models.User.id == user_id).first()
    if not owner:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    new_task = models.Task(
        title=task.title,
        description=getattr(task, "descript", None),
        owner_id=user_id,
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

