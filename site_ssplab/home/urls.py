from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('index', views.index, name = 'index'),
    path('evenements', views.evenements, name = 'evenements'),
    path('lettres', views.lettres, name = 'lettres'),
    path('team', views.team, name = 'team'),
    path('outils', views.outils, name = 'outils'),
    path('funathon', views.funathon, name = 'funathon'),
    path('seminaires', views.seminaires, name = 'seminaires'),
    path('pres', views.pres, name = 'pres'),
]
