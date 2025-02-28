from django.db import models

class Mecanico(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome