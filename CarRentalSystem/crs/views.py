from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LoginForm, RegistrationForm
from .models.reservation import Reservation, CarModel
from .models.user import User
from .forms import ReservationForm  # Import your Reservat

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Process login data
            # Example: authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.get(username=username, password=password)
            # Redirect to dashboard/home if authenticated
            return redirect('dashboard')  # Assuming 'dashboard' is the URL name for the user's dashboard
    else:
        form = LoginForm()
    return render(request, 'crs/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process registration data
            # Example: create a new user
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create(username=username, email=email, password=password)
            # Redirect to login page after successful registration
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'crs/register.html', {'form': form})

def dashboard(request):
    # Your dashboard view logic goes here if you change home to reservations it will show
    return render(request, 'crs/home.html') 

class ReservationView(View):
    template_name = 'crs/reservations.html'
    model = Reservation
    form_class = ReservationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


def load_car_model(request):
    pickup_date = request.GET.get('pickup_date')
    return_date = request.GET.get('return_date')
    location = request.GET.get('location')

    print(pickup_date, return_date, location)

    car_models = CarModel.objects.filter(
        available_from_date__lte=pickup_date,
        available_to_date__gte=return_date
    )
    print(car_models)
    context = {
        'car_models': car_models,
    }
    return render(request, 'load_model.html', context)