from django.conf.urls import url

from . import views

app_name = 'fftree'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^class/(?P<init_year>[0-9]+)/$', views.pledgeClass, name='pledgeClass'),
	url(r'^brother/(?P<brother_id>[0-9]+)/$', views.brother, name='brother'),
	url(r'^brother/(?P<brother_id>[0-9]+)/comment/$', views.comment, name='comment'),
]