from django.db import models

class Model_Short(models.Model):
    long_url = models.URLField("URL") #for my link
    short_url = models.Field() #for storing
    def __str__(self):
        return self.long_url #uniquetogether