from django.conf.urls import patterns, url
from . import views

urlpatterns = [
	url(r'^$', views.Index, name='Index'),
	url(r'^sign$', views.sign, name='sign'),
	url(r'^deco$', views.logout, name='logout'),
	url(r'^login$', views.login, name='login'),
	url(r'^newsign$', views.newsign, name='newsign'),
]