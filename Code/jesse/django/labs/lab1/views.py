from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponse

from .models import TodoItem

# Create your views here.
def home(request):
    items = TodoItem.objects.all()

    context = {
        'items': items
    }
    return render(request, 'lab1/index.html', context)

def save(request):
    name = request.POST['item']
    model = TodoItem(name=name)
    model.save()
    print(request.POST)
    return HttpResponseRedirect(reverse('lab1:home'))