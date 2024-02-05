from django.db import models
from django.urls import reverse

class Flyrod (models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    line_weight = models.CharField(max_length=20)
    description = models.TextField(max_length=250)

    def __def__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('rod_detail', kwargs={'flyrod_id': self.id})


class Flyreel (models.Model):
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    line_weights = models.CharField(max_length=20)
    description = models.TextField(max_length=250)

    def __def__(self):
        return self.name
    