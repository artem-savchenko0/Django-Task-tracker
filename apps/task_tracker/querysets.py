from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TaskQuerySet(models.QuerySet):
    def for_user(self, user: User) -> "TaskQuerySet":
        return self.filter(user=user)

    def todo(self) -> "TaskQuerySet":
        return self.filter(status=self.model.Status.TODO)

    def in_progress(self) -> "TaskQuerySet":
        return self.filter(status=self.model.Status.IN_PROGRESS)

    def done(self) -> "TaskQuerySet":
        return self.filter(status=self.model.Status.DONE)
