from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('musica/',include('disco.urls', namespace = 'disco')),
    path('', include('core.urls', namespace = 'index')),
]
