from django.db import models
from ..tasks import execute_reminder


class Reminder(models.Model):
    post_url = models.URLField()
    text = models.TextField()
    delay = models.IntegerField()

    def __str__(self):
        return self.post_url

    def save(self, *args, **kwargs):
        super(Reminder, self).save(*args, **kwargs)
        if self.delay:
            seconds = self.delay * 60
            execute_reminder.apply_async((self.pk,), countdown=seconds)
            pass
