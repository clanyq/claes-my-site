from django.contrib import admin
from feedapp.models import News, Press, UserProfile, Document
# Register your models here.

admin.site.register(News)
admin.site.register(Press)
admin.site.register(UserProfile)
admin.site.register(Document)