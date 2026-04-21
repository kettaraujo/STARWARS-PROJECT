from django.shortcuts import render, redirect
from .models import Jedi
from .forms import JediForm


def lista_jedi(request):
    jedis = Jedi.objects.all()

    return render(request, 'cadastro/lista_jedi.html', {
        'jedis': jedis
    })


def criar_jedi(request):
    form = JediForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('lista_jedi')

    return render(request, 'cadastro/criar_jedi.html', {
        'form': form
    })