from django.conf.urls import url
from feedapp import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^news/$', views.all_news, name='news'),
        url(r'^press/$', views.press, name='press'),
        url(r'^news/(?P<news_name_slug>[\w\-]+)/$', views.show_news, name='show_news'),


]
