# oficina/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import home  # Importe a view da página inicial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Página inicial
    path('clientes/', include('clientes.urls')),
    path('veiculos/', include('veiculos.urls')),
    path('mecanicos/', include('mecanicos.urls')),
    path('servicos/', include('servicos.urls')),
    path('pecas/', include('pecas.urls')),
    path('ordens/', include('ordens.urls')),
    path('dashboard/', include('dashboard.urls')),
]