from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Explo
import datetime

# Create your views here.

def liste_explo(request):
    explo = Explo.objects.all().filter(date_fin__gte = datetime.date.today())
    anciennes_explorations = Explo.objects.all().filter(date_fin__lt = datetime.date.today())

    data = {'explorations': explo, 'anciennes_explorations': anciennes_explorations}
    return render(request, 'explo/explo.html', data)

def exploration(request,name):
    try:
        exploration = Explo.objects.get(slug=name)
        data = {'exploration':exploration}
    except:
        data = {'exploration','Cette exploration n\'existe pas'}
    return render(request, 'explo/detail_explo.html', data)


