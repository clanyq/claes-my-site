from __future__ import unicode_literals

from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=2000)
    pubdate = models.DateField()

    def __str__(self):
        return(self.title + ' : ' + self.body + ' : ' + str(self.pubdate))
