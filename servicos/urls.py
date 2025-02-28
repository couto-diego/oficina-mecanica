# servicos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.servico_list, name='servico_list'),
    path('novo/', views.servico_create, name='servico_create'),
    path('editar/<int:pk>/', views.servico_update, name='servico_update'),
    path('excluir/<int:pk>/', views.servico_delete, name='servico_delete'),
]