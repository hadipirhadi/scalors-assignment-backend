from rest_framework import serializers

from ..models import TblTodo


class TblTodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TblTodo
        fields = "__all__"
