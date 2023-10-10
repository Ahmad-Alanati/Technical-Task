from django.urls import path
from .views import RegistrationView,CustomLoginView,HomeView,AboutView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path("", HomeView.as_view(), name="index"),
    path("SignUp/", RegistrationView.as_view(), name="registration"),
    path('Login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
]
