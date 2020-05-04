from django.db import models

# Create your models here.

class model_short(models.Model):
    long_url = models.URLField("URL", unique=True) #for my link
    short_url = models.CharField(max_length=20) #for storing
    def __str__(self):
        return self.long_url
