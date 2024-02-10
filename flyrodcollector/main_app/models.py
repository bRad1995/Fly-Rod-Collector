from django.db import models
from django.urls import reverse

TRIPS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

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
    
    def get_absolute_url(self):
        return reverse('reel_detail', kwargs={'flyreel_id': self.id})
  
    

class Trip (models.Model):
    date = models.DateField('fishing date')
    trip = models.CharField(
        max_length=1,
        choices=TRIPS,
        default=TRIPS[0][0],
        )
    
    flyrod = models.ForeignKey(Flyrod, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_trip_display()} on {self.date}"
    
    class Meta: 
        ordering = ['-date']
    