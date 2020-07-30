from django.contrib import admin
from django.urls import path,re_path
from . import views
urlpatterns = [
    re_path('^$',views.index),
    re_path('^resiger$',views.resiger1),
    re_path('^save$', views.save_uid),
    re_path('^text_swiper$', views.swiper),
     re_path('^login', views.login),
    re_path('^article', views.article),
]
