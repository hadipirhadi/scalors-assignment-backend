from django.db import models

from .board_model import Board


class TblTodo(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    boards = models.ForeignKey(Board, related_name='todolist', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
