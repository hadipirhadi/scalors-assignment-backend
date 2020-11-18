from rest_framework import viewsets, mixins

from ..models.reminder_model import Reminder
from ..serializers import ReminderSerializer


class ReminderViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
