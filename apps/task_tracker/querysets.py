from django.db import models


class TaskQuerySet(models.QuerySet):
	def for_user(self, user):
		return self.filter(user=user)
	
	def todo(self):
		return self.filter(status="todo")
	

	def completed(self):
		return self.filter(status="done")