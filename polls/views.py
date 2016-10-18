from django.shortcuts import render

from .models import Dados


def index(request):
    ult_temperatura = Dados.objects.order_by('-data')[:1]
    ult_umidade = Dados.objects.order_by('-data')[:1]
    context = {'ult_temperatura': ult_temperatura,'ult_umidade':ult_umidade}
    return render(request, 'polls/index.html', context)

