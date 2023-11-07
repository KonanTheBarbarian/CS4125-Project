from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from .models import User

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

def reservations(request):
    # Your reservations view logic goes here
    return render(request, 'crs/reservations.html')  # Assuming 'reservations.html' is your reservations page template