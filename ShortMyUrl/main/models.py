from django.db import models
import uuid
# Create your models here.

class Model_Short(models.Model):
    long_url = models.URLField("URL") #for my link
    short_url = models.UUIDField(default='') #for storing
    def __str__(self):
        return self.long_url
