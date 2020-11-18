# Create your views here.
# from django.http import HttpResponse
from rest_framework import viewsets

from ..models.board_model import Board
from ..serializers.board_serializer import BoardSerializer


class BoardView(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardViewDetail(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
