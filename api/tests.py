from django.test import TestCase
from .models import Task, Users


class TaskTestCase(TestCase):
    def setUp(self):
        self.user = Users.objects.create(username="usuario1")
        self.user2 = Users.objects.create(username="usuario2")

    def test_create_task(self):
        Task.objects.create(description='Test Task user1', status='Created', user_id=self.user)
        task = Task.objects.all()[0]
        self.assertEqual(len(Task.objects.all()), 1)
        self.assertEqual(task.user_id.id, self.user.id)
        self.assertEqual(task.description, 'Test Task user1')
        self.assertEqual(task.status, 'Created')
