from django import forms
from .models import Airline, Airport


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
        help_texts = {
            "airline_name": "Enter full airline name",
            "airline_code": "Enter three digit airline code",
            "founded": "Enter date when the airline was founded",
            "headquarters_city_code": "Enter three letter city code",
        }

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

class JustButtonForm(forms.Form):
    """
    Empty form for just button needs
    """