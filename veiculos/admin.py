# veiculos/admin.py
from django.contrib import admin
from .models import Veiculo

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'placa', 'cliente')
    search_fields = ('marca', 'modelo', 'placa')
    list_filter = ('marca', 'cliente')