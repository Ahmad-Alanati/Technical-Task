from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.shortcuts import redirect
from django.contrib.auth import login


# Create your views here.
class RegistrationView(CreateView):
    template_name = "sign_up.html"
    form_class = SignUpForm
    success_url = reverse_lazy('Login')
    def form_valid(self, form):
        email = form.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            form.add_error('email', 'This email address already exist.')
            return self.form_invalid(form)
        user = form.save()
        login(self.request, user)  
        return redirect('home')
    
    

class CustomLoginView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy('home')
    
class HomeView(TemplateView):
    template_name = "homepage.html"
    
class AboutView(TemplateView):
    template_name = "about.html"