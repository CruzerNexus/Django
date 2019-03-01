import datetime

from django.db import models
from django.utils import timezone


class GroceryItem(models.Model):
    text_description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date published')
    completed_date = models.DateTimeField('date completed', null=True, blank=True)
    completed_yn = models.BooleanField(default=False)

    def __str__(self):
        return self.text_description

    def was_published_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)
