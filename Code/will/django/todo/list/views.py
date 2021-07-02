from django.shortcuts import render, reverse
from .models import MyModel
from django.http import HttpResponseRedirect

# Create your views here.


def checklist(request):
    myinstances = MyModel.objects.all()
    context = {
        'myinstances': myinstances
    }
    return render(request, 'todo/mytemplate.html', context)


def mycreate(request):
    myfield = request.POST['myfield']
    mymodel = MyModel(myfield=myfield)
    mymodel.save()
    return HttpResponseRedirect(reverse('list:checklist'))
