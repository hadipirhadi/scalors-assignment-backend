from rest_framework import serializers
from .models import TblTodo


class TblTodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
