from django.conf.urls import url
from feedapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news/$', views.news_list, name='news'),
    url(r'^press/$', views.press_list, name='press'),
    url(r'^news/(?P<news_name_slug>[\w\-]+)/$', views.news_detail, name='show_news'),
]
