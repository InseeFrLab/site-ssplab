from django.contrib import admin
from .models import ExpeR


class ExpeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_debut')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(ExpeR, ExpeAdmin)