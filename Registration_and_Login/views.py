from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .models import Auth_user

# Create your views here.
class RegistrationView(CreateView):
    template_name = "sign_up.html"
    fields = ['username', 'email', 'password']
    

class LoginView(TemplateView):
    template_name = "login.html"