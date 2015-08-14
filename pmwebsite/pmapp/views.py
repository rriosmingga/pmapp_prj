from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from pmapp.models import *


def index(request):
    lista_partidos = Partido.objects.order_by('date')[:10]
    context = {'lista_partidos' : lista_partidos}
    return render(request, 'pmapp/index.html', context)
    
def teamdetail(request, equipo_id):
	response = "Estas en la pagina del equipo %s."
	return HttpResponse(response % equipo_id)
	
def matchdetail(request, partido_id):
	partido = Partido.objects.get(pk=partido_id)
	pronosticos = PartidoPronostico.objects.filter(match_id=partido_id)
	local = 0; empate = 0; visita = 0; total = 0
	for pronostico in PartidoPronostico.objects.filter(match_id=partido_id):
		if pronostico.gteam1 > pronostico.gteam2:
			aux = 100 * pronostico.gteam1 + pronostico.gteam2
			local = local + 1
		elif pronostico.gteam1 < pronostico.gteam2:
			visita = visita + 1
		else:
			empate = empate + 1
	total = local + empate + visita
	if total > 0:
		local = (local * 100)/total 
		empate = (empate * 100)/total
		visita = (visita * 100)/total
	context = {'partido' : partido, 'pronosticos' : pronosticos, 'total' : total, 'local' : local, 'empate' : empate, 'visita' : visita}
	return render(request, 'pmapp/matchdetail.html', context)