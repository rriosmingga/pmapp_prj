from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from django.core.urlresolvers import reverse

from pmapp.models import *


def index(request):
    lista_partidos = Partido.objects.order_by('date')[:10]
    context = {'lista_partidos' : lista_partidos}
    return render(request, 'pmapp/index.html', context)
    
def teamdetail(request, equipo_id):
	response = "Estas en la pagina del equipo %s."
	return HttpResponse(response % equipo_id)
	
def matchdetail(request, partido_id):
	try:
		partido = Partido.objects.get(pk=partido_id)
		pronosticos = PartidoPronostico.objects.filter(match_id=partido_id)
		local = 0; empate = 0; visita = 0; total = 0
		resultados = []
		for pronostico in PartidoPronostico.objects.filter(match_id=partido_id):
			resultados.append(str(pronostico.gteam1) + ' - ' + str(pronostico.gteam2))
			if pronostico.gteam1 > pronostico.gteam2:
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
		context = {'partido' : partido, 'pronosticos' : pronosticos, 'resultados' : resultados, 'total' : total, 'local' : local, 'empate' : empate, 'visita' : visita}
	except Partido.DoesNotExist:
		return HttpResponse('No existe el partido')
		
	return render(request, 'pmapp/matchdetail.html', context)

def predict(request, partido_id):
	try:
		match = Partido.objects.get(id=partido_id)
		user = User.objects.get(username=request.POST['userlogin'])
		pronostico = PartidoPronostico(
							match=match,
							user=user,
							gteam1=request.POST['gteam1'],
							gteam2=request.POST['gteam2']
		)
		pronostico.save()
	except Partido.DoesNotExist:
		return HttpResponse('No existe el partido')
	except IntegrityError:
		match_obj = PartidoPronostico.objects.get(match=match,user=user)
		match_obj.gteam1=request.POST['gteam1']
		match_obj.gteam2=request.POST['gteam2']
		match_obj.save()
		return HttpResponseRedirect(reverse('pmapp:matchdetail', args=(partido_id)))
		
	
	return HttpResponseRedirect(reverse('pmapp:matchdetail', args=(partido_id)))
