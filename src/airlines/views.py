from airlines.models import Airline, Airport
from django.shortcuts import render
from django.db.models import Q

import airlines
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from airlines.forms import AirlineModelForm, AirportModelForm, JustButtonForm


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

    def get_queryset(self):
        queryset = super().get_queryset()

        # test if it is passing the parameters
        print(self.kwargs)

        start_str = self.kwargs.get('start_str')
        if start_str:
            queryset = queryset.filter(
                Q(airline_name__startswith=start_str) |
                Q(airline_name__icontains=start_str) |
                Q(airline_code__icontains=start_str)
            )

        return queryset


class AirlinesDetailView(DetailView):
    template_name = "airline_detail_template.html"
    model = Airline
    context_object_name = "airline"

class AirlinesCreateView(CreateView):
    template_name = "airline_create_template.html"
    model = Airline
    form_class = AirlineModelForm

    def get_success_url(self):
        # Access the updated object using self.object
        pk = self.object.pk
        # Generate the success URL dynamically using the object's pk
        return reverse_lazy("airlines:detail-view", kwargs={"pk": pk})

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

    def get_success_url(self):
        # Access the updated object using self.object
        pk = self.object.pk
        # Generate the success URL dynamically using the object's pk
        return reverse_lazy("airlines:detail-view", kwargs={"pk": pk})
#------------------------------------------------------------------------
# AIRPORT VIEWS
#------------------------------------------------------------------------
class AirportListView(ListView):
    template_name = "airport_listing_template.html"
    model = Airport
    context_object_name = "airports"

    def get_queryset(self):
        queryset = super().get_queryset()

        # test if it is passing the parameters
        print(self.kwargs)

        start_str = self.kwargs.get('start_str')
        print(self.request.GET)
        if start_str:
            queryset = queryset.filter(airport_name__startswith=start_str)
            #     Q(airport_name__icontains=start_str) |
            #     Q(airport_code__icontains=start_str)
            # )
        return queryset

class AirportDetailView(DetailView):
    template_name = "airport_detail_template.html"
    model = Airport
    context_object_name = "airport"

class AirportsCreateView(CreateView):
    template_name = "airport_create_template.html"
    form_class = AirportModelForm

    def get_success_url(self):
        # Access the updated object using self.object
        pk = self.object.pk
        # Generate the success URL dynamically using the object's pk
        return reverse_lazy("airlines:airport-detail-view", kwargs={"pk": pk})

class AirportDeleteView(DeleteView):
    template_name = "airport_delete_view.html"
    model = Airport
    context_object_name = "airport"
    success_url = reverse_lazy("airlines:airport-list-view")

class AirportsUpdateView(UpdateView):
    template_name = "airport_update_view.html"
    model = Airport
    form_class = AirportModelForm

    def get_success_url(self):
        # Access the updated object using self.object
        pk = self.object.pk
        # Generate the success URL dynamically using the object's pk
        return reverse_lazy("airlines:airport-detail-view", kwargs={"pk": pk})