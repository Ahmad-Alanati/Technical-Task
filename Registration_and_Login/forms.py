from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'custom-input', 'id': 'username-input'})
    )
    email = forms.EmailField(required=True,
    help_text="example@example.com",
    widget=forms.EmailInput(attrs={'class': 'custom-input', 'id': 'email-input'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'custom-input', 'id': 'password1-input'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'custom-input', 'id': 'password2-input'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == 'admin':
            raise forms.ValidationError('The username "admin" is not allowed.')
        return username

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1:
            try:
                password_validation.validate_password(password1, self.instance)
            except forms.ValidationError as error:
                raise forms.ValidationError(error.messages)

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('The passwords do not match.')

        return password2
    
class LoginForm(AuthenticationForm):
    pass