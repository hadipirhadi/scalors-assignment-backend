#from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .models import TblTodo
from .serializers import TblTodoSerializer


#def index(request):
#    return render(request, 'todo/todolist.html')
class TblTodoView(viewsets.ModelViewSet):
    queryset = TblTodo.objects.all()
    serializer_class = TblTodoSerializer
