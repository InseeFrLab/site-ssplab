from datetime import datetime
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ExpeR
import datetime

# Create your views here.

def liste_expe(request):
    experimentations = ExpeR.objects.all().filter(date_fin__gte = datetime.date.today())
    anciennes_experimentations = ExpeR.objects.all().filter(date_fin__lt = datetime.date.today())

    data = {'experimentations': experimentations, 'anciennes_experimentations': anciennes_experimentations}
    return render(request, 'expe/expe.html', data)

def experimentation(request,name):
    try:
        experimentation = ExpeR.objects.get(slug=name)
        data = {'experimentation':experimentation}
    except:
        data = {'experimentation','Cette experimentation n\'existe pas'}
    return render(request, 'expe/detail_expe.html', data)