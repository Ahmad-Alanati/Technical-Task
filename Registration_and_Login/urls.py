from django.urls import path
from .views import RegistrationView,LoginView

urlpatterns = [
    # path("", HomeView.as_view(), name="index"),
    path("SignUp/", RegistrationView.as_view(), name="registration"),
    path("Login/", LoginView.as_view() , name="Login")
]
