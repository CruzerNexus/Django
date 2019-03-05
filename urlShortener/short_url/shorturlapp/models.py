from django.db import models


class NewUrl(models.Model):
    code = models.CharField(max_length=6)
    url = models.TextField()
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.code
