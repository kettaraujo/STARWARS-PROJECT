from django.shortcuts import render
from .models import Treinamento, Missao


def lista_treinamentos(request):
    treinamentos = Treinamento.objects.all()

    return render(request, 'treinamentos/lista_treinamentos.html', {
        'treinamentos': treinamentos
    })

def lista_missoes(request):
    missoes = Missao.objects.all()

    return render(request, 'treinamentos/lista_missoes.html', {
        'missoes': missoes
    })