from django.db import models
import datetime

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Article(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField()
    author = models.CharField(max_length=200)
    created_on  = models.DateField(default=datetime.date.today)
    hashtag = models.CharField(max_length = 50, default = '')
    categories = models.CharField(max_length = 100, default = '')
    image_titre = models.CharField(max_length = 100, default = '')
    slug = models.SlugField(max_length=200, unique=True, null= True, blank=False)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title