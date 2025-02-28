# pecas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.peca_list, name='peca_list'),
    path('novo/', views.peca_create, name='peca_create'),
    path('editar/<int:pk>/', views.peca_update, name='peca_update'),
    path('excluir/<int:pk>/', views.peca_delete, name='peca_delete'),
]