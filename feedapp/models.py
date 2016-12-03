from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=2000,)
    pubdate = models.DateField()

    def __str__(self):
        return(self.title)


class Press(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    source = models.CharField(max_length=50)
    pubdate = models.DateField()

    def __str__(self):
        return(self.title)


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return (self.user)