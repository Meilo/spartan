from django.conf.urls import patterns, url
from . import views

urlpatterns = [
	url(r'^$', views.CreateList, name='CreateList'),
	url(r'^profil$', views.Profil, name='Profil')
]