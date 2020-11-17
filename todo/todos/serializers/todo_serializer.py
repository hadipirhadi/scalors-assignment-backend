from rest_framework import serializers

from ..models import TblTodo


class TblTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblTodo
        # fields = ["name", "todolists"]
        fields = "__all__"
