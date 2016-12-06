from django.conf.urls import url
from feedapp import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^input/$', views.input_form, name='input_site'),
        url(r'^news/$', views.all_news, name='news'),
        url(r'^press/$', views.press, name='press'),
        url(r'^news/(?P<news_name_slug>[\w\-]+)/$', views.show_news, name='show_news'),
]
