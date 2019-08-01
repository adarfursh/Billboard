from django.conf.urls import include,url
from . import views
from django.contrib import admin
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^posts/', views.list, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, kwargs={'next_page': '/login'},name='logout'),
    url(r'^register/$', views.register, name='register'),
]