# oficina/views.py
from django.shortcuts import render
from dashboard.models import MetricasDashboard

def home(request):
    metricas, created = MetricasDashboard.objects.get_or_create(pk=1)
    metricas.atualizar_metricas()
    return render(request, 'home.html', {'metricas': metricas})