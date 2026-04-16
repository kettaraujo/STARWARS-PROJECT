from django.db import models

class Personagem(models.Model):
    RANKS = [
        ('Padawan', 'Padawan'),
        ('Cavaleiro', 'Cavaleiro Jedi'),
        ('Mestre', 'Mestre Jedi'),
    ]

    nome = models.CharField(max_length=200)
    codigo_jedi = models.CharField(max_length=50)
    base = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    rank = models.CharField(max_length=20, choices=RANKS)

    foto = models.ImageField(upload_to='fotos/')
    logo_empresa = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.nome