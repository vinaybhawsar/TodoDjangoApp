from django.db import models
from django.conf import settings


# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=60)
    created_date = models.DateField(auto_now_add=True)

    @property
    def task_count(self):
        return self.tasks.all().count()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Task List"
        verbose_name_plural = "Task Lists"


class Task(models.Model):
    title = models.CharField(max_length=140)
    task_list = models.ForeignKey(TaskList,
                                  related_name="tasks",
                                  on_delete=models.CASCADE,
                                  null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        related_name="todo_created_by",
        on_delete=models.CASCADE,
    )
    priority = models.PositiveIntegerField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["priority", "created_date"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
