"""Urls for todo_app service APIs."""
from rest_framework.routers import DefaultRouter

from todo_manager.views import (TaskViewSet, TaskListViewSet)

router = DefaultRouter()

# Custom Routes
router.register('task', TaskViewSet, basename='task_operations')
router.register('task-list', TaskListViewSet, basename='task_list_operations')

urlpatterns = router.urls
