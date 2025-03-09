from airlines.models import Airline, Airport
from django.shortcuts import render

import airlines
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from airlines.forms import AirlineModelForm, JustButtonForm


#------------------------------------------------------------------------
# AIRLINE VIEWS
#------------------------------------------------------------------------
def airline_home_page(request):
    """Airlines home page"""
    return render(request, 'home_page.html')

class AirlinesListingView(ListView):
    template_name = "airline_listing_template.html"
    model = Airline
    context_object_name = "airlines"

class AirlinesDetailView(DetailView):
    template_name = "airline_detail_template.html"
    model = Airline
    context_object_name = "airline"

class AirlinesCreateView(CreateView):
    template_name = "airline_create_template.html"
    model = Airline
    form_class = AirlineModelForm
    success_url = reverse_lazy("airlines:list-view")

class AirlineDeleteView(DeleteView):
    template_name = "airline_delete_template.html"
    model = Airline
    context_object_name = "airline"
    success_url = reverse_lazy("airlines:list-view")
    form_class = JustButtonForm

class AirlinesUpdateView(UpdateView):
    template_name = "airline_update_template.html"
    model = Airline
    form_class = AirlineModelForm
    success_url = reverse_lazy("airlines:list-view")

    # def get_success_url(self):
    #     return reverse_lazy('airlines:airline-detail', kwargs={'pk': self.object.pk})

#------------------------------------------------------------------------
# AIRPORT VIEWS
#------------------------------------------------------------------------
class AirportListView(ListView):
    template_name = "airport_listing_template.html"
    model = Airport
    context_object_name = "airports"

class AirportDetailView(DetailView):
    template_name = "airport_detail_template.html"
    model = Airport
    context_object_name = "airport"