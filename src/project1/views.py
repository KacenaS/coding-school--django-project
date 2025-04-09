from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView, RedirectView
from django.http import HttpResponse, HttpResponseRedirect

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, message="You are logged in.")
            return redirect('home')
        else:
            messages.error(request, message='Username OR password is incorrect')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.error(request, message="You have been logged out.")
    return HttpResponseRedirect(reverse_lazy('home'))
