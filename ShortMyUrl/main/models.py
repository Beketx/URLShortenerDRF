from django.db import models

# Create your models here.

class Model_Short(models.Model):
    short_url = models.CharField(max_length=50) #for storing
    long_url = models.URLField("URL", unique=True) #for my link
    def __str__(self):
        return self.long_url
