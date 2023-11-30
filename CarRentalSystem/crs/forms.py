# Import necessary Django modules
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from crs.models.reservation import Reservation

# LoginForm 
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#  RegistrationForm with unique username and email validation
class RegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with this username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email

# ReservationForm 
class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['name', 'model', 'pickup_date', 'return_date', 'location', 'is_under_25', 'is_child_seat', 'year', 'penalty_point']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'pickup_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'return_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.Select(attrs={'class': 'form-control'}),
            'is_under_25': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_child_seat': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'penalty_point': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Penalty points',
                'style': 'display: none',
            }),
        }
