from django import forms
from .models import Airline, Airport
from django.core.exceptions import ValidationError

class AirlineModelForm(forms.ModelForm):
    class Meta:
        model = Airline
        fields = "__all__"
        labels = {
            "airline_name": "Airline name",
            "airline_code": "Airline code",
            "founded": "Founded",
            "headquarters_city_code": "Headquarters city code",
        }
        widgets = {
            'alliance': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
        help_texts = {
            "airline_name": "Enter full airline name",
            "airline_code": "Enter three digit airline code",
            "founded": "Enter date when the airline was founded",
            "headquarters_city_code": "Enter three letter city code",
        }

    def clean_airline_name(self):
        """Checking for duplicate data"""
        airline_name = self.cleaned_data.get('airline_name')

        dupe_airline = Airline.objects.filter(airline_name=airline_name).exclude(pk=self.instance.pk).exists()
        if dupe_airline:
            raise ValidationError("Airline name already exists")

        return airline_name

class AirportModelForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = "__all__"
        labels = {
            "airport_name": "Airport name",
            "country_code": "Country code",
            "city_code": "City code",
            "airport_code": "Airport code",
        }
        help_texts = {
            "airport_name": "Enter full airport name",
            "country_code": "Enter two letter country code",
            "city_code": "Enter three letter city code",
            "airport_code": "Enter three letter airport code",

        }

    def clean_airport_name(self):
        """Checking for duplicate data"""

        airport_name = self.cleaned_data.get("airport_name")

        dupe_airline = Airport.objects.filter(airport_name=airport_name).exclude(pk=self.instance.pk).exists()
        if dupe_airline:
            raise ValidationError("Airport name already exists")

        return airport_name


class JustButtonForm(forms.Form):
    """
    Empty form for just button needs
    """