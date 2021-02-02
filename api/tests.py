from django.test import TestCase


# Create your tests here.

class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="usuario1")
        self.user2 = User.objects.create(username="usuario2")
