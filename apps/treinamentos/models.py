from django.db import models
from cadastro.models import Personagem
from datetime import timedelta
from django.utils import timezone

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    carga_horaria = models.IntegerField()
    validade_meses = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Missao(models.Model):
    jedi = models.ForeignKey(Personagem, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    data_inicio = models.DateField()
    observacoes = models.TextField(blank=True)
    anexo = models.FileField(upload_to='missoes/', null=True, blank=True)

    def data_vencimento(self):
        return self.data_inicio + timedelta(days=30 * self.curso.validade_meses)

    def dias_para_vencer(self):
        return (self.data_vencimento() - timezone.now().date()).days

    def status(self):
        dias = self.dias_para_vencer()

        if dias < 0:
            return "Vencido"
        elif dias <= 10:
            return "Crítico"
        elif dias <= 30:
            return "Alerta"
        elif dias <= 60:
            return "Atenção"
        elif dias <= 90:
            return "Planejamento"
        return "OK"

    def __str__(self):
        return f"{self.jedi.nome} - {self.curso.nome}"