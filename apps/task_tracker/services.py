from django.contrib.auth import get_user_model
from .models import Task

User = get_user_model()

def create_task(*, user: User, title: str, description: str = "", priority: int) -> Task:
	task = Task(
		user=user,
		title=title,
		description=description,
		priority=priority,
)
	task.full_clean()
	task.save()
	return task 

def change_status(*, task: Task, status: str) -> Task:
	task.status = status
	task.full_clean()
	task.save(update_fields=["status"])
	return task

