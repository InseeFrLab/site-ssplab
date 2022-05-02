from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def evenements_view(request):
    return render(request, 'home/evenements.html')

def team_view(request):
    return render(request, 'home/team.html')

def lettres_view(request):
    return render(request, 'home/lettres_BD.html')

def pres_view(request):
    return render(request, 'home/presentation_generale.html')

def outils_view(request):
    return render(request, 'home/tools.html')

def funathon_view(request):
    return render(request, 'home/funathon.html')

def seminaires_view(request):
    return render(request, 'home/detail_seminaires.html')

def communaute_view(request):
    return render(request, 'home/communaute.html')