from django.conf.urls import url
from pressapp import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^pressform/$', views.press_form, name='press_form'),
]