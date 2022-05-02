from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.liste_expe, name = 'expe'),
    path('experimentation/<slug:name>/', views.experimentation, name ='experimentation')]

