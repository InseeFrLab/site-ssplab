from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

# Create your views here.

def blog_index(request):
    articles = Article.objects.all()
    data = {'articles': articles}
    return render(request, 'blog/blog_index.html', data)

def article(request,name):
    try:
        article = Article.objects.get(slug=name)
        data = {'article':article}
    except:
        data = {'article','Cet article n\'existe pas'}
    return render(request, 'blog/article.html', data)