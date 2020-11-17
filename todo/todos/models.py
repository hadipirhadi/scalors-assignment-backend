from django.db import models


# Create your models here.
# from todo.board.models import Board


class TblTodo(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # board = models.ForeignKey(Board, related_name='todolist', on_delete=models.CASCADE)

    def __str__(self):
        return  self.title

