from django.shortcuts import render
from django.views.generic import ListView, DetailView


# Create your views here.

def semin(request):
    return render(request, 'semin/semin.html')