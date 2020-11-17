from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from rest_framework import viewsets
from .models import Board
from .serializers import BoardSerializer


class BoardView(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


# def index(request):
#     return HttpResponse("Hello world")
