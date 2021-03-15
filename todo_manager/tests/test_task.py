from rest_framework import status
from rest_framework.test import APITestCase
from todo_manager.models import Task, TaskList


class TaskListTests(APITestCase):
    base_url = "/api/v1/task/"

    def setUp(self):
        self.task_list = TaskList.objects.create(name="Test List")
        self.task = Task.objects.create(title="Test",
                                        task_list=self.task_list,
                                        priority=1,
                                        completed=False)

    def test_get_all_task(self):
        """
        Ensure we can get list of task list object.
        """
        response = self.client.get(self.base_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['title'],
                         self.task.title)

    def test_get_task_by_id(self):
        """
        Ensure we can get task list object by id.
        """
        response = self.client.get(f"{self.base_url}{self.task.id}/",
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'],
                         self.task.title)

    def test_create_task(self):
        """
        Ensure we can create a new task list object.
        """
        data = {
            'title': 'SampleList',
            'task_list_id': self.task_list.id,
            'priority': 2,
            'completed': False
        }
        response = self.client.post(self.base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.get(title=data['title']).title,
                         response.json()['title'])

    def test_update_task(self):
        """
        Ensure we can update task list object.
        """
        data = {
            'title': 'SampleList',
            'task_list_id': self.task_list.id,
            'priority': 2,
            'completed': False
        }
        response = self.client.put(f"{self.base_url}{self.task.id}/",
                                   data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], data['title'])

    def test_delete_task(self):
        """
        Ensure we can delete task list object.
        """
        response = self.client.delete(f"{self.base_url}{self.task.id}/",
                                      format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.filter(id=self.task.id).first(),
                         None)
