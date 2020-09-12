from django.contrib import admin
from django.urls import path,re_path
from . import views
import myapp1
from django.conf.urls import handler404, handler500
app_name='myapp1'
urlpatterns = [
    re_path('^article/support', views.support),
    re_path('^$',views.main_all),
    re_path('^resiger$',views.resiger1),
    re_path('^save$', views.save_uid),
    re_path('^login$', views.login),
    re_path('^article', views.article),
    re_path('^time$', views.time),
    re_path('^nowlogin$', views.now_login),
    re_path('^verifycode$', views.verifycode),
    re_path('^main', views.main),
    re_path('^all$', views.main_all),

]

#
