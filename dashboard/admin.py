# dashboard/admin.py
from django.contrib import admin
from .models import MetricasDashboard

@admin.register(MetricasDashboard)
class MetricasDashboardAdmin(admin.ModelAdmin):
    list_display = ('total_os', 'total_faturamento', 'data_atualizacao')
