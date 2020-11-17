from django.contrib import admin

from .models.board_model import Board
# Register your models here.
from .models.todo_model import TblTodo

admin.site.register(TblTodo)
admin.site.register(Board)
