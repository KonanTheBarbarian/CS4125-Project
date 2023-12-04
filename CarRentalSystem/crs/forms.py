from django import forms
from django.core.exceptions import ValidationError
from crs.models.reservation import Reservation
from users.models import CustomUser

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Date of Birth")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email
    

    
class ReservationForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(ReservationForm, self).__init__(*args, **kwargs)
    #     self.fields['model'] = Reservation.objects.all()

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


#class VehicleForm(forms.ModelForm):
 #   class Meta:
  #      model = Vehicle
   #     fields = ['make', 'model', 'year', 'color', 'price']

    #    widgets = {
     #       'make': forms.TextInput(attrs={'class': 'form-control'}),
      #      'model': forms.TextInput(attrs={'class': 'form-control'}),
       #     'year': forms.NumberInput(attrs={'class': 'form-control'}),
        #    'color': forms.TextInput(attrs={'class': 'form-control'}),
         #   'price': forms.NumberInput(attrs={'class': 'form-control'}),
        #}