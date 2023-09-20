from datetime import datetime
from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel

from models import TaskModel
from demo_tasks import demo_tasks

# App
router = APIRouter(
    prefix="/api",
    tags=["tasks"],
)


# -- Tasks --
# Read
class GetTasksResponse(BaseModel):
    tasks: List[TaskModel]


@router.get("/tasks")
async def get_tasks() -> GetTasksResponse:
    return GetTasksResponse(
        tasks=[TaskModel(
            id=t.id,
            name=t.name,
            completed=t.completed,
        ) for t in demo_tasks.get_tasks()],
    )


# Update
class UpdateTaskRequest(BaseModel):
    task_id: UUID
    name: str


@router.post("/tasks/update")
async def update_task(
    request: UpdateTaskRequest,
) -> None:
    task = demo_tasks.get_task(request.task_id)
    if task is None:
        raise Exception
    task.name = request.name


class ToggleTaskCompleteRequest(BaseModel):
    task_id: UUID
    completed: Optional[datetime]


@router.post("/tasks/complete")
async def toggle_task_complete(
    request: ToggleTaskCompleteRequest,
) -> None:
    task = demo_tasks.get_task(request.task_id)
    if task is None:
        raise Exception
    task.completed = request.completed


# Delete
class DeleteTaskRequest(BaseModel):
    task_id: UUID


@router.post("/tasks/delete")
async def delete_task(
    request: DeleteTaskRequest,
) -> None:
    demo_tasks.delete_task(request.task_id)
