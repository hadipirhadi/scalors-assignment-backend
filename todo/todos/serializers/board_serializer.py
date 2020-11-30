from rest_framework import serializers
from ..models.board_model import Board


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    todos = serializers.StringRelatedField(many=True)
    total_todos = serializers.SerializerMethodField(read_only=True)
    total_uncompleted = serializers.SerializerMethodField(read_only=True)

    @staticmethod
    def get_total_todos(board):
        return board.todos.count()

    @staticmethod
    def get_total_uncompleted(board):
        return board.todos.filter(done=False).count()

    class Meta:
        model = Board
        fields = ['name', 'todos', 'total_todos', 'total_uncompleted']


# class NameSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Board
#         fields = "name"

# class BoardOnlySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Board
#         fields = "__all__"
