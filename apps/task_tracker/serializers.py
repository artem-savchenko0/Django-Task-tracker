from rest_framework import serializers
from .models.task import Task
from django.utils import timezone

class TaskSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source="get_status_display", read_only=True)
    priority_display = serializers.CharField(source="get_priority_display", read_only=True)
    is_overdue = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"


        read_only_fields = [
            "id", 
            "user", 
            "created_at", 
            "updated_at", 
            "status", 
            "status_display", 
            "is_overdue"
        ]

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return value

    def get_is_overdue(self, obj):
        if obj.deadline and obj.status != Task.Status.DONE:
            return obj.deadline < timezone.now()
        return False

    def validate(self, attrs):
        if self.instance and self.instance.status == Task.Status.TODO and attrs.get("status") == Task.Status.DONE:
            raise serializers.ValidationError("Task must be in progress before completion")
        return attrs
