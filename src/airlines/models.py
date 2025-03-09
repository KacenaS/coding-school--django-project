from django.db import models
from datetime import datetime
from django.urls import reverse_lazy

class Aliance(models.Model):
    """Shows to which aliance does each airline belong to"""
    name = models.CharField(max_length=50)

# Basic airline model
class Airline(models.Model):
    airline_name = models.CharField(max_length=100, blank=True)
    airline_code = models.IntegerField(null=True)
    founded = models.DateField(null=True, blank=True)
    headquarters_city_code = models.CharField(max_length=3, blank=True)
    # headquarters_city_name = models.CharField(max_length=100)
    # headquarters_country = models.CharField(max_length=2)

    # relationships
    # aliance = models.ManyToManyField(Aliance, null=True, blank=True)
    # many-to-many relationship to airports missing !
    # aliance = models.ManyToManyField(Aliance) ?
    # airports = models.ManyToManyField('Airport') ?

    # fuction to update the airline code to 3  digits
    """
    def airline_code_converter(self):
        airlines = Airline.objects.all()
        for airline in airlines:
            # Convert airline_code to a string
            code = str(airline.airline_code)

            # Check if the length is 2
            if len(code) == 2:
                # Add a leading zero
                airline.airline_code = "0" + code
            return airline.airline_code
            """

    def __str__(self):
        return self.airline_name


# Basic airport model
class Airport(models.Model):
    airport_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2)
    city_code = models.CharField(max_length=3)
    airport_code = models.CharField(max_length=4, unique=True)

    # relationships
    # many-to-many relationship to airlines missing !

    def __str__(self):
        return self.airport_name