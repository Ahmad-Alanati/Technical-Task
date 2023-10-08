from django.urls import path
from .views import RegistrationView,CustomLoginView,HomeView

urlpatterns = [
    # path("", HomeView.as_view(), name="index"),
    path("SignUp/", RegistrationView.as_view(), name="registration"),
    path('Login/', CustomLoginView.as_view(), name='login'),
    path('', HomeView.as_view(), name='home'),
]
