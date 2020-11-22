from django.db import models
from django.db.models import ForeignKey

from .board_model import Board
from django.contrib.auth.models import User


class TblTodo(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, related_name='todos', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos',
                              null=True, blank=True, default=None)

    def __str__(self):
        return self.title
