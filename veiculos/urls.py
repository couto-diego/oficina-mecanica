# veiculos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.veiculo_list, name='veiculo_list'),
    path('novo/', views.veiculo_create, name='veiculo_create'),
    path('editar/<int:pk>/', views.veiculo_update, name='veiculo_update'),
    path('excluir/<int:pk>/', views.veiculo_delete, name='veiculo_delete'),
]