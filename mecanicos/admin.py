# mecanicos/admin.py
from django.contrib import admin
from .models import Mecanico

@admin.register(Mecanico)
class MecanicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'especialidade')
    search_fields = ('nome', 'especialidade')
    list_filter = ('especialidade',)
