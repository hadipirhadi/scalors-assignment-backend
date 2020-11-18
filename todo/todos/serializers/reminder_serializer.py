from rest_framework import serializers

from ..models import Reminder


class ReminderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reminder
        fields = ('url', 'post_url', 'text', 'delay')


class ReminderSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = ('__all__')

