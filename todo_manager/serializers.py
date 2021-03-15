"""
Serializer for related to todo_app.
"""
from rest_framework import serializers
from todo_manager.models import Task, TaskList


class TaskSerializer(serializers.ModelSerializer):
    """A serializer for Task."""

    class Meta:
        model = Task
        fields = "__all__"


class TaskDetailSerializer(serializers.ModelSerializer):
    """A serializer for Task."""

    class Meta:
        depth = 1
        model = Task
        fields = "__all__"


class TaskListSerializer(serializers.ModelSerializer):
    """A serializer for Task List."""

    class Meta:
        model = TaskList
        fields = ("id", "name", "created_date", "task_count")
