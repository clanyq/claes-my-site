from django.contrib import admin
from feedapp.models import News, Press, Image
# Register your models here.

admin.site.register(News)
admin.site.register(Press)
admin.site.register(Image)