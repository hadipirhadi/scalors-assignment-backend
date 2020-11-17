from rest_framework import serializers
from .models import Board
from ..todos.serializers import TblTodoSerializer


class BoardSerializer(serializers.ModelSerializer):
    todolists = TblTodoSerializer()

    class Meta:
        model = Board
        fields = ["name", "todolists"]
