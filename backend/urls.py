from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clientes.urls')),  # Esto apunta a tus endpoints API
    path('clientes/', include('clientes.urls')),  # Esto apunta a los templates HTML
]