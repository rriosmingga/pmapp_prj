from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from pmapp.models import Equipo, Partido


def index(request):
    lista_partidos = Partido.objects.order_by('-pk')[:10]
    context = {'lista_partidos' : lista_partidos}
    return render(request, 'pmapp/index.html', context)
    
def teamdetail(request, equipo_id):
	response = "Estas en la pagina del equipo %s."
	return HttpResponse(response % equipo_id)
	
def matchdetail(request, partido_id):
	partido = Partido.objects.get(pk=partido_id)
	context = {'partido' : partido}
	return render(request, 'pmapp/matchdetail.html', context)