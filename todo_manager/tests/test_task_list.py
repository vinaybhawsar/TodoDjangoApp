from rest_framework import status
from rest_framework.test import APITestCase
from todo_manager.models import TaskList


class TaskListTests(APITestCase):
    base_url = "/api/v1/task-list/"

    def setUp(self):
        self.task_list = TaskList.objects.create(name="Test List")

    def test_get_all_task_list(self):
        """
        Ensure we can get list of task list object.
        """
        response = self.client.get(self.base_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(response.json()['results'][0]['name'],
                         self.task_list.name)

    def test_get_task_list_by_id(self):
        """
        Ensure we can get task list object by id.
        """
        response = self.client.get(f"{self.base_url}{self.task_list.id}/",
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'],
                         self.task_list.name)

    def test_create_task_list(self):
        """
        Ensure we can create a new task list object.
        """
        data = {'name': 'SampleList'}
        response = self.client.post(self.base_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TaskList.objects.get(name=data['name']).name,
                         response.json()['name'])

    def test_update_task_list(self):
        """
        Ensure we can update task list object.
        """
        data = {'name': 'SampleList'}
        response = self.client.put(f"{self.base_url}{self.task_list.id}/",
                                   data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], data['name'])

    def test_delete_task_list(self):
        """
        Ensure we can delete task list object.
        """
        response = self.client.delete(f"{self.base_url}{self.task_list.id}/",
                                      format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TaskList.objects.filter(id=self.task_list.id).first(),
                         None)
