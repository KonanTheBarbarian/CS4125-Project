from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LoginForm, RegistrationForm
from .models.reservation import Reservation, CarModel
from .models.user import User
from .forms import ReservationForm  # Import your Reservat

#Imports for Inventory System
from django.shortcuts import render, redirect
from .models.vehicle import Vehicle
from .Inventory.vehConBuilder import ConcreteVehicleBuilder
from .Inventory.vehDirector import VehicleDirector
from django.contrib import messages

from django.contrib.auth.decorators import user_passes_test

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Process login data
            # Example: authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.get(username=username, password=password)
            return redirect('dashboard') 
    else:
        form = LoginForm()
    return render(request, 'crs/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            date_of_birth = form.cleaned_data['date_of_birth']
            user, created = User.objects.get_or_create(username=username, email=email)
            if created:
                user.set_password(password)
                user.save()

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


#@user_passes_test(lambda u: u.is_superuser)
def add_vehicle(request):
    if request.method == 'POST':
        model_name = request.POST.get('model_name')
        year = request.POST.get('year')
        price = request.POST.get('price')
        available_from_date = request.POST.get('available_from_date')
        available_to_date = request.POST.get('available_to_date')
        location = request.POST.get('location')

        # Create a director and a concrete builder
        builder = ConcreteVehicleBuilder()
        director = VehicleDirector(builder)

        # Construct the vehicle using the director
        director.construct(model_name, year, price, available_from_date, available_to_date, location)
        vehicle_dict = builder.get_result()

        # Save the vehicle to the database
        vehicle_instance = Vehicle(**vehicle_dict)
        vehicle_instance.save()

        messages.success(request, 'Vehicle added successfully')

        # You may want to add additional error handling and validation here

        return redirect('inventory')  # Assuming you have a URL named 'vehicle_list'

    return render(request, 'crs/inventory.html')