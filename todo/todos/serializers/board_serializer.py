from rest_framework import serializers

from .todo_serializer import TblTodoSerializer
from ..models.board_model import Board


class BoardSerializer(serializers.ModelSerializer):
    todolists = TblTodoSerializer()

    class Meta:
        model = Board
        fields = ["name", "todolists"]
