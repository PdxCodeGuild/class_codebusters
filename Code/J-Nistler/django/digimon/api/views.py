from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Level, Digimon

# Create your views here.
def home (request):
    return HttpResponse('Okay')
    
# Retreive
def get_digimon(request, mon):

    try:
        mon = Digimon.objects.filter(name=mon)[0]
        digimon = {
            'name' : mon.name,
            'img' : mon.img,
            'level' : mon.level.evolution
        }
    except:
        digimon = {
            'error': 'Digimon not found'
        }
    return JsonResponse(digimon)

# List
def all_digimon(request):
    mons = list(Digimon.objects.all().values())

    # output = []

    # for mon in mons:
    #     output.append({
    #         'name': mon.name,
    #         'img' : mon.img,
    #         'level' : mon.level.evolution,
    #     })
    
    return JsonResponse(mons, safe=False)