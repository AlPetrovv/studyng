from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request: HttpRequest):
    return HttpResponse("Страница приложения")

def categories(request: HttpRequest):
    return HttpResponse('<h1>Cat</h1>')