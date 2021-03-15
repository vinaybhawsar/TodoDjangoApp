from django.contrib import admin
from todo_manager.models import Task, TaskList

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskList)
