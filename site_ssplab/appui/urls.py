from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.liste_appui, name = 'appui'),
    path('appui/<slug:name>/', views.appui, name ='appui_detaille')]
