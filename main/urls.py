"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from home.views import index, evenements_view, team_view, pres_view, outils_view, lettres_view, funathon_view, seminaires_view, communaute_view
#from blog.views import blog_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'home'),
    path('blog/', include('blog.urls')),
    path('expe/', include('expe.urls')),
    path('explo/', include('explo.urls')),
    path('semin/', include('semin.urls')),
    path('appui/', include('appui.urls')),
    path('outils/', outils_view, name = 'outils'),
    path('evenements/', evenements_view, name = 'evenements'),
    path('funathon/', funathon_view, name = 'funathon'),
    path('seminaires/', seminaires_view, name = 'seminaires'),
    path('communaute/', communaute_view, name = 'seminaires'),
    path('lettres/', lettres_view, name = 'lettres'),
    path('team/',team_view, name = "equipe"),
    path('index/',index, name = "home"),
    path('pres/',pres_view, name = "pres"),
]
