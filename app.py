from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from datetime import datetime

from tasks import TaskList

# Create the app
app = FastAPI()


tasks = TaskList()
tasks.add_task('test')


paginate_limit = 10


# -- Tasks --
# Create
@app.post("/api/tasks")
async def add_task(
    name: str,
):
    tasks.add_task(name)


# Read
@app.get("/api/tasks")
async def get_tasks(
    # task_id: Optional[int],
    # page_number: Optional[int],
):
    # input
    # - parent_task_id for filtering
    # - page_number, default 1

    # processing
    # - paginate by paginate_limit
    #   - if he asks for page 11 but there's only 10 pages available, return an empty array with the other fields correct
    # - filter by parent_task_id, if null return all

    # output
    # - tasks array
    # - has_children bool
    # - current_page_number
    # - paginate_limit

    # if task_id is None:
    return tasks.get_tasks_as_dicts()
    # else:
    # return tasks.get_task(task_id)


# Update
@app.post("/api/tasks/update")
async def update_task(
    task_id: int,
    name: str,
):
    tasks.update_task(task_id, name)


# Delete


# -- TaskEvents --
# Play
@app.post("/api/tasks/play")
async def play_task(
    task_id: int,
    time_iso_string: str,
):
    task = tasks.get_task(task_id)[0]
    time = datetime.fromisoformat(time_iso_string)
    task.start_event(time)


# Pause
@app.post("/api/tasks/pause")
async def pause_task(
    task_id: int,
    time_iso_string: str,
):
    task = tasks.get_task(task_id)[0]
    time = datetime.fromisoformat(time_iso_string)
    task.stop_event(time)


# Static Front End
app.mount("/", StaticFiles(directory="dist", html=True), name="static")
