from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Todo
from .serializers import TodoSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [AllowAny]
