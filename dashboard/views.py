from django.shortcuts import render
from django.db.models import Count, Sum, Case, When, IntegerField
from ordens.models import OrdemServico
from .models import MetricasDashboard
from datetime import datetime

def dashboard(request):
    # Atualizar métricas gerais
    metricas, created = MetricasDashboard.objects.get_or_create(pk=1)
    metricas.atualizar_metricas()

    # Dados para gráficos
    ordens_por_status = OrdemServico.objects.values('status').annotate(total=Count('id'))
    ordens_por_status_labels = [item['status'] for item in ordens_por_status]
    ordens_por_status_data = [item['total'] for item in ordens_por_status]

    # Faturamento mensal (ano corrente)
    ano_corrente = datetime.now().year
    faturamento_mensal = OrdemServico.objects.filter(data_emissao__year=ano_corrente).values('data_emissao__month').annotate(total=Sum('valor_total'))
    faturamento_mensal_labels = [f"Mês {item['data_emissao__month']}" for item in faturamento_mensal]
    faturamento_mensal_data = [float(item['total']) for item in faturamento_mensal]  # Converter Decimal para float

    # Faturamento semestral
    faturamento_semestral = OrdemServico.objects.filter(data_emissao__year=ano_corrente).annotate(
        semestre=Case(
            When(data_emissao__month__lte=6, then=1),
            When(data_emissao__month__gt=6, then=2),
            output_field=IntegerField(),
        )
    ).values('semestre').annotate(total=Sum('valor_total'))
    faturamento_semestral_labels = [f"Semestre {item['semestre']}" for item in faturamento_semestral]
    faturamento_semestral_data = [float(item['total']) for item in faturamento_semestral]

    # Faturamento anual
    faturamento_anual = OrdemServico.objects.filter(data_emissao__year=ano_corrente).aggregate(total=Sum('valor_total'))
    faturamento_anual_total = float(faturamento_anual['total'] or 0)

    context = {
        'metricas': metricas,
        'ordens_por_status_labels': ordens_por_status_labels,
        'ordens_por_status_data': ordens_por_status_data,
        'faturamento_mensal_labels': faturamento_mensal_labels,
        'faturamento_mensal_data': faturamento_mensal_data,
        'faturamento_semestral_labels': faturamento_semestral_labels,
        'faturamento_semestral_data': faturamento_semestral_data,
        'faturamento_anual_total': faturamento_anual_total,
        'ano_corrente': ano_corrente,  # Adicionar o ano corrente ao contexto
    }
    return render(request, 'dashboard/dashboard.html', context)