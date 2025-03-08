from django.db import models
from django.urls import reverse_lazy

class Airline(models.Model):
    name = models.CharField(max_length=100)

