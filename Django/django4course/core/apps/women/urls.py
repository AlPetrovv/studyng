from django.urls import path

from .views import index, categories

urlpatterns = [
    path('women/', index),
    path('categories/', categories)
]