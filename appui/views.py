from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import AppuiR
import datetime

# Create your views here.

def liste_appui(request):
    appuis = AppuiR.objects.all().filter(date_fin__gte = datetime.date.today())
    anciens_appuis = AppuiR.objects.all().filter(date_fin__lt = datetime.date.today())

    data = {'appuis': appuis, 'anciens_appuis': anciens_appuis}
    return render(request, 'appui/appui.html', data)


def appui(request,name):
    try:
        appui = AppuiR.objects.get(slug=name)
        data = {'appui':appui}
    except:
        data = {'appui','Ce soutien méthodologique n\'existe pas'}
    return render(request, 'appui/detail_appui.html', data)