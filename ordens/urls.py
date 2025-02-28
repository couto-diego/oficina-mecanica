# ordens/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ordem_servico_list, name='ordem_servico_list'),
    path('novo/', views.ordem_servico_create, name='ordem_servico_create'),
    path('editar/<int:pk>/', views.ordem_servico_update, name='ordem_servico_update'),
    path('excluir/<int:pk>/', views.ordem_servico_delete, name='ordem_servico_delete'),
]