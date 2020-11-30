from django.urls import path, include
from rest_framework import routers

from . import views
from .views import BoardList, BoardDetail

router = routers.DefaultRouter()
router.register('todo', views.TblTodoView)
router.register('board', views.BoardView, basename='board')
router.register('reminders', views.ReminderViewSet)
# router.register('users', views.UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('', BoardList.as_view()),
    path('<int:id>', BoardDetail.as_view()),
]
