from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('reservations/', views.reservations, name='reservations'),

]
