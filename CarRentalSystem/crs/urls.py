from django.urls import path
from . import views
from .views import SynchronizeDBView
from django.contrib.auth import views as auth_views

app_name = 'crs'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reservations/', views.ReservationView.as_view(), name='reservations'),
    path('load-car-models/', views.load_car_model, name='load_car_models'),
    path('inventory/', views.add_vehicle, name='inventory'),
    path('synchronize-db/', SynchronizeDBView.as_view(), name='synchronize_db'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('reservationsuccess/', views.reservationsuccess, name='reservationsuccess'),
]