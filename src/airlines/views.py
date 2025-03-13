from airlines.models import Airline, Airport
from django.shortcuts import render
from django.db.models import Q

import airlines
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from airlines.forms import AirlineModelForm, AirportModelForm, JustButtonForm
from pyexpat.errors import messages
from django.contrib import messages


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

        start_str = self.request.GET.get('start_str')
        if start_str:
            queryset = queryset.filter(
                Q(airline_name__icontains=start_str) |
                Q(airline_code__icontains=start_str)
            )

        return queryset

class AirlinesDetailView(DetailView):
    template_name = "airline_detail_template.html"
    model = Airline
    context_object_name = "airline"

class AirlinesCreateView(LoginRequiredMixin,CreateView):
    template_name = "airline_create_template.html"
    model = Airline
    form_class = AirlineModelForm
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return self.object.get_absolute_url()

    def dispatch(self, request, *args, **kwargs):
        """Gives error message when not logged in"""
        if not request.user.is_authenticated:
            messages.error(request, message='You have to login to Create a new Airline.')
        return super().dispatch(request, *args, **kwargs)

class AirlineDeleteView(LoginRequiredMixin,DeleteView):
    template_name = "airline_delete_template.html"
    model = Airline
    context_object_name = "airline"
    success_url = reverse_lazy("airlines:list-view")
    form_class = JustButtonForm
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        """Gives error message when not logged in"""
        if not request.user.is_authenticated:
            messages.error(request, message='You have to login to Delete this Airline.')
        return super().dispatch(request, *args, **kwargs)

class AirlinesUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "airline_update_template.html"
    model = Airline
    form_class = AirlineModelForm
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        """Gives error message when not logged in"""
        if not request.user.is_authenticated:
            messages.error(request, message='You have to login to Update Airlines.')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.object.get_absolute_url()
#------------------------------------------------------------------------
# AIRPORT VIEWS
#------------------------------------------------------------------------
class AirportListView(ListView):
    template_name = "airport_listing_template.html"
    model = Airport
    context_object_name = "airports"

    def get_queryset(self):
        """Fetches customer imput for filtering airline data"""
        queryset = super().get_queryset()

        start_str = self.request.GET.get('start_str')

        if start_str:
            queryset = queryset.filter(
                Q(airport_name__icontains=start_str) |
                Q(airport_code__icontains=start_str)
            )
        return queryset

class AirportDetailView(DetailView):
    template_name = "airport_detail_template.html"
    model = Airport
    context_object_name = "airport"

class AirportsCreateView(LoginRequiredMixin, CreateView):
    template_name = "airport_create_template.html"
    form_class = AirportModelForm
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        """Gives error message when not logged in"""
        if not request.user.is_authenticated:
            messages.error(request, message='You have to login to Create a new Airport.')
        return super().dispatch(request, *args, **kwargs)


    def get_success_url(self):
        return self.object.get_absolute_url()

class AirportDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "airport_delete_view.html"
    model = Airport
    context_object_name = "airport"
    success_url = reverse_lazy("airlines:airport-list-view")
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        """Gives error message when not logged in"""
        if not request.user.is_authenticated:
            messages.error(request, message='You have to login to Delete Airport.')
        return super().dispatch(request, *args, **kwargs)

class AirportsUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "airport_update_view.html"
    model = Airport
    form_class = AirportModelForm
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        """Gives error message when not logged in"""
        if not request.user.is_authenticated:
            messages.error(request, message='You have to login to Update Airport.')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.object.get_absolute_url()