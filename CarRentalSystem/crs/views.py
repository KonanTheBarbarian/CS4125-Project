from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LoginForm, RegistrationForm
from .models.reservation import Reservation, CarModel
#from .models.user import User
from .forms import ReservationForm 
from django.contrib.auth import  login

from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

#Imports for Inventory System
from django.shortcuts import render, redirect
from .models.vehicle import Vehicle
from .Inventory.vehConBuilder import ConcreteVehicleBuilder
from .Inventory.vehDirector import VehicleDirector
from django.contrib import messages

#user imports new
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
from users.models import CustomUser

#import for sync functionality 
from .management.commands import copy_data  # Import the Command class
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Process login data
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(f"Attempting login for user: {email}")
            print(f"Password entered: {password}")

            try:
                user_db = CustomUser.objects.get(email=email)
                print(f"User {email} exists in the database.")

                # Check the password
                if check_password(password, user_db.password):
                    # Password is correct, log in the user
                    login(request, user_db)
                    print(f"Login successful for user: {email}")
                    return redirect('crs:dashboard')  
                else:
                    print("Incorrect password")
            except CustomUser.DoesNotExist:
                print(f"User {email} does not exist in the database.")

            print("Fail to login...")
            # Invalid login
            return render(request, 'crs/login.html', {'form': form, 'error_message': 'Invalid login credentials'})

    else:
        form = LoginForm()

    return render(request, 'crs/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            date_of_birth = form.cleaned_data['date_of_birth']

            # Use make_password to hash the password
            hashed_password = make_password(password)

            # Create a new user instance with the hashed password
            user, created = CustomUser.objects.get_or_create(
                email=email,
                defaults={
                    'password': hashed_password,
                    'date_of_birth': date_of_birth,
                    'accountType': 'customer',  # or whatever default value you want
                }
            )

            if not created:
                # If the user already exists, update the fields except for the password
                user.date_of_birth = date_of_birth
                user.accountType = 'customer'  
                user.save()

            # Log in the user after successful registration
            login(request, user)
            return redirect('crs:dashboard')  # Redirect to your dashboard or desired page

    else:
        form = RegistrationForm()

    return render(request, 'crs/register.html', {'form': form})




def logoutUser(request):

    logout(request)
   
    return redirect('crs:dashboard')


#@login_required
def dashboard(request):
   # print(f"Is user authenticated? {request.user.is_authenticated}")
   # print(f"Template Context: {request.__dict__}")
    return render(request, 'crs/home.html', {'user': request.user}) 

def aboutus(request):
    # Your view logic here
    return render(request, 'crs/aboutus.html')

def reservationsuccess(request):
    # Your view logic here
    return render(request, 'crs/reservationsuccess.html')



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
            return redirect('crs:reservationsuccess')
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



def is_staff_user(CustomUser):
    return CustomUser.is_authenticated and CustomUser.accountType == "staff"

@user_passes_test(is_staff_user)
def add_vehicle(request):

    vehicles = Vehicle.objects.all()[:10]
    context = {
        'vehicles': vehicles,
    }

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
        
        return redirect('crs:inventory')  

    return render(request, 'crs/inventory.html', context)


#Function to synchronise the inventory and car_model tables
class SynchronizeDBView(View):
    def get(self, request, *args, **kwargs):
        # Run the synchronization command
        command = copy_data.Command()
        command.handle()

        # Redirect to the original page 
        return HttpResponseRedirect(reverse('crs:inventory'))
    
    def post(self, request, *args, **kwargs):
        command = copy_data.Command()
        command.handle()
        return HttpResponseRedirect(reverse('crs:inventory'))
    

    
    