from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete

from django.template.defaultfilters import slugify


class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pubdate = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return(self.title)

    class Meta:
        verbose_name_plural = 'News'


class Press(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    source = models.CharField(max_length=50)
    pubdate = models.DateField(auto_now_add=True)


    def __str__(self):
        return(self.title)

    class Meta:
        verbose_name_plural = 'Press'


class Image(models.Model):

    imgfile = models.ImageField(upload_to='images/')
    

    def __str__(self):
        return (str(self.imgfile))


# @receiver(pre_delete, sender=Image)
# def image_delete(sender, instance, **kwargs):

#     instance.imgfile.delete(False)