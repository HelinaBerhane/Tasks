from tasks import Task, TaskList
from datetime import datetime, timezone


def populate_demo_tasks(task_list, info):
    for name, completed in info:
        datetime.now().isoformat()
        task_list.add_task(Task(
            name=name,
            completed=completed,
        ))


demo_tasks_info = [
    (
        'front end - reusable components - complete button',
        datetime(2023, 9, 13, 12, 59, 5, tzinfo=timezone.utc),
    ),
    (
        'front end - reusable components - toggle complete button',
        datetime(2023, 9, 13, 14, 38, tzinfo=timezone.utc),
    ),
    (
        'front end - reusable components - delete button',
        datetime(2023, 9, 11, 18, 30, 8, tzinfo=timezone.utc),
    ),
    (
        'front end - reusable components - front end - inline edit text',
        datetime(2023, 9, 14, 6, 30, 51, tzinfo=timezone.utc),
    ),
    (
        'front end - reusable components - front end - inline edit in a task list item',
        datetime(2023, 9, 16, 14, 6, 0, tzinfo=timezone.utc),
    ),
    (
        'Complete Tasks - front end - storybook components - task text changes',
        datetime(2023, 9, 13, 14, 38, tzinfo=timezone.utc),
    ),
    (
        'Complete Tasks - back end - endpoints',
        datetime(2023, 9, 13, 14, 38, tzinfo=timezone.utc),
    ),
    (
        'Complete Tasks - front end - full implementation - make text more faint when complete',
        datetime(2023, 9, 13, 14, 52, tzinfo=timezone.utc),
    ),
    (
        'Complete Tasks - front end - full implementation - move completed tasks to the bottom of the page',
        datetime(2023, 9, 13, 15, 58, 10, tzinfo=timezone.utc),
    ),
    (
        'Create Tasks - back end - endpoints',
        None,
    ),
    (
        'Create Tasks - front end - full implementation',
        None,
    ),
    (
        'Update Tasks - back end - endpoints',
        datetime(2023, 9, 14, 13, 23, 45, tzinfo=timezone.utc),
    ),
    (
        'Update Tasks - front end - full implementation',
        datetime(2023, 9, 20, 13, 5, tzinfo=timezone.utc),
    ),
    (
        'Delete Tasks - back end - endpoints',
        datetime(2023, 9, 20, 11, 53, tzinfo=timezone.utc),
    ),
    (
        'Delete Tasks - front end - full implementation',
        datetime(2023, 9, 20, 11, 53, tzinfo=timezone.utc),
    ),
    (
        'Persisting Tasks',
        None,
    ),
    (
        'front end - reusable components - front end - date picker',
        None,
    ),
    (
        'front end - reusable components - front end - task picker',
        None,
    ),
    (
        'Task Events',
        None,
    ),
    (
        'Repeating Tasks',
        None,
    ),
    (
        'Parent Tasks',
        None,
    ),
    (
        'Local DB for offline use',
        None,
    ),
    (
        'consider using elasticsearch for read heavy parts of the code',
        None,
    ),
    (
        'consider using a graph database for relationship heavy parts of the code',
        None,
    ),
    (
        'read about using recursive queries for relationship heavy parts of the code https://www.postgresql.org/docs/current/queries-with.html',
        None,
    ),
    (
        'read about using ltree for hierarchy heavy parts of the code https://www.postgresql.org/docs/current/ltree.html',
        None,
    ),
]

demo_tasks = TaskList()
populate_demo_tasks(demo_tasks, demo_tasks_info)