from django.shortcuts import render

from pmapp.models import Equipo, Partido


def index(request):
    lista_partidos = Partido.objects.order_by('-pk')[:2]
    context = {'lista_partidos' : lista_partidos}
    return render(request, 'pmapp/index.html', context)