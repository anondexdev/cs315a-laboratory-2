from typing import List, Optional
from pydantic import BaseModel,ConfigDict

class TaskBase(BaseModel):
    title: str
    descript: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    completed: bool
    owner_id: int

    model_config = ConfigDict(from_attributes=True)


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    tasks: List[TaskResponse] = []

    model_config = ConfigDict(from_attributes=True)from typing import List, Optional
from pydantic import BaseModel,ConfigDict

class TaskBase(BaseModel):
    title: str
    descript: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    completed: bool
    owner_id: int

    model_config = ConfigDict(from_attributes=True)


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    tasks: List[TaskResponse] = []

    model_config = ConfigDict(from_attributes=True)