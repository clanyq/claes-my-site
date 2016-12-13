from django.contrib import admin
from feedapp.models import News, Press, Image


class ArticleAdmin(admin.ModelAdmin):
   prepopulated_fields = {
   "slug": ("title",),
   }

admin.site.register(Press)
admin.site.register(Image)
admin.site.register(News, ArticleAdmin)


