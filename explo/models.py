from django.db import models
import datetime

# Create your models here.

class Explo(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    author = models.CharField(max_length=200)
    date_debut  = models.DateField(default=datetime.date.today)
    date_fin  = models.DateField(default=datetime.date.today)
    image_titre = models.CharField(max_length = 100, default = '')
    slug = models.SlugField(max_length=200, unique=True, null= True, blank=False)

    class Meta:
        ordering = ['-date_fin']
    
    def __str__(self):
        return self.title