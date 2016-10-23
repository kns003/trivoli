from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
    url(r'^travel/$', views.create_travel),
	url(r'^travel/view/$', views.view_travel),
	url(r'^travel/edit/(?P<travel_id>\d+)/$', views.handle_travel),
	url(r'^travel/delete/(?P<travel_id>\d+)/$', views.delete_travel),
	url(r'^travel/view/(?P<travel_id>\d+)/$', views.load_travel),
	url(r'^travel/create_from_file/$', views.create_from_file),
]