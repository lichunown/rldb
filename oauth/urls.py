from django.conf.urls import include, url
from django.contrib import admin
from . import views 

urlpatterns = [
    url(r'^github$', views.oauth_github,name='oauth_github'),
    url(r'^tencent$', views.oauth_tencent,name='oauth_tencent'),
    url(r'^tencent/get$', views.oauth_tencent_get,name='oauth_tencent_get'),
]