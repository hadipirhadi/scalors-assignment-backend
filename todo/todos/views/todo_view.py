from rest_framework import viewsets

from ..models.todo_model import TblTodo
from ..serializers import TblTodoSerializer


class TblTodoView(viewsets.ModelViewSet):
    queryset = TblTodo.objects.all()
    serializer_class = TblTodoSerializer



