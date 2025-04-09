from django.db import models
from datetime import datetime
from django.urls import reverse_lazy

class Alliance(models.Model):
    """Shows to which alliance does each airline belong to"""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def alliances_list_as_string(self):
        """Returns a string representation of alliance instances"""
        alliances = self.objects.all()
        return ", ".join(alliance.name for alliance in alliances)

# Basic airline model
class Airline(models.Model):
    airline_name = models.CharField(max_length=100, blank=True)
    airline_code = models.IntegerField( blank=True)
    founded = models.DateField(null=True, blank=True)
    headquarters_city_code = models.CharField(max_length=3, blank=True)

    # Many-to-many relationship with Alliance
    alliance = models.ManyToManyField(Alliance,related_name='airline_alliance', blank=True)

    def get_absolute_url(self):
        """Returns the url to access a detail page of this model"""
        return reverse_lazy('airlines:detail-view', kwargs={'pk': self.pk})

    def __str__(self):
        return self.airline_name


# Basic airport model
class Airport(models.Model):
    airport_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2)
    city_code = models.CharField(max_length=3)
    airport_code = models.CharField(max_length=4, unique=True)

    def get_absolute_url(self):
        """Returns the url to access a detail page of this model"""
        return reverse_lazy('airlines:airport-detail-view', kwargs={'pk': self.pk})

    def __str__(self):
        return self.airport_name