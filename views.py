from django.views.generic import ListView
from .models import golf_platform
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy 
from django.views.generic import CreateView 

class HomePageView(ListView):
        model = golf_platform
        template_name = "home.html"


class dashboardPageView(ListView):
        model = golf_platform
        template_name = "dashboard.html"

class aboutPageView(ListView):
        model = golf_platform
        template_name = "about.html"


class signupPageView(ListView):
        model = golf_platform
        template_name = "signup.html"


class loginPageView(ListView):
        model = golf_platform
        template_name = "login.html"


class contactPageView(ListView):
        model = golf_platform
        template_name = "contact.html"
