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
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.success(request, 'Please use the correct credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return HttpResponseRedirect(reverse_lazy('home'))


"""
class AccountLogoutConfirmationView(TemplateView):
    template_name = 'account_logout_confimation_template.html'

class AccountLogoutYesNoView(TemplateView):
    template_name = 'account_logout_yes_no_template.html'

class AccountLogoutView(RedirectView):
    url = reverse_lazy("logout-confirmation")

    logged_out_user = None

    def get(self, request, *args, **kwargs):
        self.logged_out_user = request.user
        logout(request)
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        user_pk = self.logged_out_user.pk if self.logged_out_user else ""
        return self.url + f"userid={user_pk}"

class AccountLoginView(LoginView):
    template_name = 'login_template.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy("home")

class AccountLoginConfirmationView(TemplateView):
    template_name = "account_login_confirmation_template.html"3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print(self.request.GET)
        user_pk = self.request.GET.get("user_pk")
        if user_pk:
            context['logged_user'] = User.objects.filter(pk=int(user_pk).first())
        else:
             context['logged_user'] = ""
        return context



"""
    # def form_valid(self, form):
    #     username = form.cleaned_data.get("username")
    #     password = form.cleaned_data.get("password")
    #
    #     user = authenticate(self.request, username=username, password=password)
    #     if user is not None:
    #         login(self.request, user)
    #         return HttpResponseRedirect(reverse_lazy("home"))
    #
    #     return super().form_valid(form)





"""
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return HttpResponse('Invalid username and/or password.')

def user_logout(request):
    logout(request)
    return redirect('login')
"""
