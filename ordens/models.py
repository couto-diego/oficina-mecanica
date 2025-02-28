from django.db import models
from veiculos.models import Veiculo
from mecanicos.models import Mecanico
from servicos.models import Servico
from pecas.models import Peca

class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('andamento', 'Em andamento'),
        ('finalizado', 'Finalizado'),
    ]

    data_emissao = models.DateField(auto_now_add=True)
    data_conclusao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')
    descricao_defeito = models.TextField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(Servico, through='OrdemServicoServico')
    pecas = models.ManyToManyField(Peca, through='OrdemServicoPeca', blank=True)

    def calcular_valor_total(self):
        total = sum(oss.quantidade * oss.servico.valor for oss in self.ordemservicoservico_set.all())
        total += sum(osp.quantidade * osp.peca.valor for osp in self.ordemservicopeca_set.all())
        self.valor_total = total
        self.save()

    def __str__(self):
        return f"OS {self.id} - {self.veiculo.placa}"

class OrdemServicoServico(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

class OrdemServicoPeca(models.Model):
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)