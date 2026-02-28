import django.db.models.deletion
import django.db.models.manager
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=60)),
                ("description", models.TextField(blank=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("todo", "To Do"),
                            ("in_progress", "In Progress"),
                            ("done", "Done"),
                        ],
                        db_index=True,
                        default="todo",
                        max_length=20,
                    ),
                ),
                (
                    "priority",
                    models.IntegerField(
                        choices=[(1, "Low"), (2, "Medium"), (3, "High")],
                        db_index=True,
                        default=2,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
            managers=[
                ("object", django.db.models.manager.Manager()),
            ],
        ),
    ]
