# mecanicos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mecanico_list, name='mecanico_list'),
    path('novo/', views.mecanico_create, name='mecanico_create'),
    path('editar/<int:pk>/', views.mecanico_update, name='mecanico_update'),
    path('excluir/<int:pk>/', views.mecanico_delete, name='mecanico_delete'),
]