from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Level, Digimon

# Create your views here.
def home(request):
    return render(request, 'api/index.html')

# Create

# Retreive
def get_digimon(request, mon):
    try:
        mon = Digimon.objects.filter(name__istartswith=mon)[0]
        digimon = {
            'name': mon.name,
            'img': mon.img,
            'level': mon.level.evolution
        }
    except:
        digimon = {
            'error': 'Digimon not found.'
        }
    return  JsonResponse(digimon)
# Update

# Delete

# List
def all_digimon(request):
    mons = list(Digimon.objects.all().values())
    # output = {
    #     'mons': []
    # }
    # for mon in mons:
    #     output['mons'].append({
    #         'name': mon.name,
    #         'img':  mon.img,
    #         'level': mon.level.evolution,
    #     })

    return JsonResponse(mons, safe=False)
