from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def posts_create(request):
	return	HttpResponse("<h1> Create </h1>")

def posts_detail(request): #RETRIEVE
	return	HttpResponse("<h1> Deatil </h1>")

def posts_list(request): #list items
	return	HttpResponse("<h1> List </h1>")

def posts_update(request):
	return	HttpResponse("<h1> Update </h1>")

def posts_delete(request):
	return	HttpResponse("<h1> Delete </h1>")
