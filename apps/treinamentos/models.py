from django.db import models
from apps.cadastro.models import Jedi #importa a outra tabela de cadastro


class Treinamento(models.Model): #cria outra tabela
    nome = models.CharField(max_length=200)
    carga_horaria = models.IntegerField() #inteiro
    validade = models.IntegerField(help_text="Validade em dias") #help aparece no amdin como uma dica
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    


class Missao(models.Model):
    STATUS_CHOICES = [ #tabela de opções fixas
        ('ATIVO', 'Conectado à Força'),
        ('VENCIDO', 'Desconectado da Força'),
    ]


    #on_delete=models.CASCADE significa que se o jedi for deletado as missoes dele serão apagadas
    jedi = models.ForeignKey(Jedi, on_delete=models.CASCADE) #cada missão pertence a um unico jedi
    treinamento = models.ForeignKey(Treinamento, on_delete=models.CASCADE)

    data_inicio = models.DateField()
    data_validade = models.DateField()

    status = models.CharField(max_length=10, choices=STATUS_CHOICES) #opções da tabela fixa

    relatorio = models.TextField(blank=True, null=True)
    anexo = models.FileField(upload_to='missoes/', blank=True, null=True) #upload de arquivos

    #como vai aparecer no admin
    def __str__(self):
        return f"{self.jedi.nome} - {self.treinamento.nome}"

    class Meta: #personalização do admin
        verbose_name = "Missão"
        verbose_name_plural = "Missões"