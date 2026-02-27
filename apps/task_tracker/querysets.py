from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
class TaskQuerySet(models.QuerySet):
	def for_user(self, user: User):
		return self.filter(user=user)
	
	def todo(self):
		return self.filter(status=self.model.Status.TODO)
	
	def completed(self):
		return self.filter(status=self.model.Status.DONE)