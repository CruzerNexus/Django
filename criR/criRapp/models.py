from django.db import models
from django.urls import reverse
from datetime import timedelta

class Cri(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("cri_detail", args=[str(self.id)])

    @property
    def created_updated_differ(self):
        return(self.updated - self.created) > timedelta(seconds=1)
