from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from todo_manager.models import Task, TaskList
from todo_manager.serializers import TaskSerializer, TaskDetailSerializer, \
    TaskListSerializer


# Create your views here.
class TaskViewSet(ModelViewSet):
    """A viewset that provides Task CRUD"""

    permission_classes = (AllowAny,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_fields = '__all__'

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return TaskDetailSerializer
        return self.serializer_class


class TaskListViewSet(ModelViewSet):
    """A viewset that provides Task List CRUD"""

    permission_classes = (AllowAny,)
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    filterset_fields = '__all__'
