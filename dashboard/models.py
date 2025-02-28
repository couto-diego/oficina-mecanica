from django.db import models 
from ordens.models import OrdemServico

class MetricasDashboard(models.Model):
    total_os = models.IntegerField(default=0)
    total_faturamento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def atualizar_metricas(self):
        self.total_os = OrdemServico.objects.count()
        self.total_faturamento = sum(os.valor_total for os in OrdemServico.objects.all())
        self.save()

    def __str__(self):
        return f"Métrica atualizada em {self.data_atualizacao}"
