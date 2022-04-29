from django.contrib import admin
from .models import AppuiR


class AppuiAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_debut')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(AppuiR, AppuiAdmin)