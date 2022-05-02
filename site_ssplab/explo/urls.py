from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.liste_explo, name = 'explo'),
    path('exploration/<slug:name>/', views.exploration, name ='exploration'),]