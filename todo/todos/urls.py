from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('todo', views.TblTodoView)
router.register('board', views.BoardView)
router.register('reminders', views.ReminderViewSet)
router.register('users', views.UserView)

urlpatterns = [
    path('', include(router.urls))
]
