from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', "posts.views.posts_list"),
	url(r'^create/$', "posts.views.posts_create"),
	url(r'^detail/$', "posts.views.posts_detail"),
	url(r'^update/$', "posts.views.posts_update"),
	url(r'^delete/$', "posts.views.posts_delete"),
    #url(r'^posts/$', "<appname>.views.<function_name"),	
]