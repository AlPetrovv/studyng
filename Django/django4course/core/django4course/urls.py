from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

# we can add all urls of specific app with include
urlpatterns += [
    path('', include('apps.women.urls')),
]

