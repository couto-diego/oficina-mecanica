# ordens/admin.py
from django.contrib import admin
from .models import OrdemServico, OrdemServicoServico, OrdemServicoPeca

class OrdemServicoServicoInline(admin.TabularInline):
    model = OrdemServicoServico
    extra = 1

class OrdemServicoPecaInline(admin.TabularInline):
    model = OrdemServicoPeca
    extra = 1

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'veiculo', 'status', 'valor_total', 'data_emissao')
    inlines = [OrdemServicoServicoInline, OrdemServicoPecaInline]