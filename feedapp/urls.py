from django.conf.urls import url
from feedapp import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^newsform/$', views.news_form, name='news_form'),
        url(r'^pressform/$', views.press_form, name='press_form'),
]
