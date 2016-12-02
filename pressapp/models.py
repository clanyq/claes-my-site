from __future__ import unicode_literals


from django.db import models

# Create your models here.

class Press(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    source = models.CharField(max_length=50)
    pubdate = models.DateField()

    def __str__(self):
        return(self.title + ' : ' + self.url + ' : ' + self.source + ' : ' + str(self.pubdate))
