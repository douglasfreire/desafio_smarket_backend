from rest_framework.viewsets import ModelViewSet
from .serializers import UsersSerializer, TaskSerializer
from .models import Users, Task
from rest_framework.response import Response


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        user_id = request.query_param.get('user_id')
        if user_id:
            self.queryset = Task.objects.filter(user_id=user_id)

        serializer = TaskSerializer(self.queryset, many=True)
        return Response(serializer.data)
