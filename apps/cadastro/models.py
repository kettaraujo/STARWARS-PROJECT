from django.db import models #importa sist django

class Jedi(models.Model): #cria uma tabela no BDD chamada jedi
    RANK_CHOICES = [ #cria opções fixas 
        ('PADAWAN', 'Padawan'), #salva como maiusculo e mostra minusculo
        ('CAVALEIRO', 'Cavaleiro Jedi'),
        ('MESTRE', 'Mestre Jedi'),
    ]
    #campos da tabela 
    nome = models.CharField(max_length=200)
    codigo_jedi = models.CharField(max_length=50, unique=True) #unique=true nao permite duplicados tipo cpf 
    templo = models.CharField(max_length=100)
    turno = models.CharField(max_length=100)
    rank = models.CharField(max_length=20, choices=RANK_CHOICES) #campo com as opções fixas

    foto = models.ImageField(upload_to='jedi_fotos/') #faz o upload de imagem e salva na url media/jedi_fotos
    emblema = models.ImageField(upload_to='emblemas/')

    #define como aparece no admin 
    def __str__(self):
        return self.nome