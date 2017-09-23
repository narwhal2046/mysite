"""mysite blog URL Configuration"""
from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^about/', views.about, name = 'about'),
]
