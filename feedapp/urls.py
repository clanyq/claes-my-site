from django.conf.urls import url
from feedapp import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^newsform/$', views.news_form, name='news_form'),
        url(r'^pressform/$', views.press_form, name='press_form'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^pic_upload/$', views.pic_upload, name='pic_upload'),
        url(r'^input/$', views.admin_site, name='input_site'),
        url(r'^news/$', views.all_news, name='news'),
        url(r'^press/$', views.press, name='press'),
        url(r'^news/(?P<news_name_slug>[\w\-]+)/$', views.show_news, name='show_news'),
]
