from django.conf.urls import url
from newsapp import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^newsform/$', views.news_form, name='news_form'),
]
