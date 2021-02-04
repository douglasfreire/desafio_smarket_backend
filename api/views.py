from rest_framework.viewsets import ModelViewSet
from .serializers import UsersSerializer, TaskSerializer
from .models import Users, Task


class UsersViewSet(ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
