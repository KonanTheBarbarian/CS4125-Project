from django.contrib import admin

#configures the Django admin interface for managing
from crs.models.reservation import  Features
from crs.models.reservation import Reservation
from crs.models.car import Car
from crs.models.reservation import CarModel
#from crs.models.user import User
from users.models import CustomUser

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'model_name', 'price', 'location', 'available_from_date', 'available_to_date', 'created_at']
    #list_display = ['id', 'model_name', 'years_no_claims', 'price', 'location', 'available_from_date', 'available_to_date', 'created_at']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'pickup_date', 'return_date', 'is_under_25', 'location', 'created_at']


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'name', 'created_at']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'year', 'price', 'created_at']

"""
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'accountType', 'date_of_birth', 'is_staff', 'is_superuser')
    search_fields = ('email', 'accountType')
    list_filter = ('accountType', 'is_staff', 'is_superuser')
    ordering = ('email',)
"""