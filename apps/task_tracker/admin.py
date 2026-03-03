from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title", 
        "user", 
        "status", 
        "priority", 
        "created_at", 
        "description", 
        "deadline", 
        "updated_at"
)       
    list_filter = ("status", "priority", "deadline")
