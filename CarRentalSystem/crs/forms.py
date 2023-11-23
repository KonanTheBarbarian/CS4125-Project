from django import forms
from crs.models.reservation import Reservation
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


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
