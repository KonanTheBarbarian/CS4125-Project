from django.db import models


# location choices dropdown data for reservation locations
LOCATION_CHOICES = (
    ('Dublin', 'Dublin'),
    ('Cork', 'Cork'),
    ('Limerick', 'Limerick'),
)

# CarModel class to represent different models of cars in the database.
class CarModel(models.Model):

    model_name = models.CharField(max_length=255, unique=True)
    year = models.CharField(max_length=4)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    available_from_date = models.DateField(null=True)
    available_to_date = models.DateField(null=True)
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Specify custom table name car_models in the database
    class Meta:
        db_table = 'car_models'

# Return model name when the object is printed
    def __str__(self):
        return self.model_name

# Features class to store features associated with each car model.
class Features(models.Model):

    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='features')
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'features'

    def __str__(self):
        return self.model.model_name

# Reservation class to handle user reservations.
class Reservation(models.Model):

    name = models.CharField(max_length=255, null=True)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='reservations')
    location = models.CharField(max_length=255, null=True)
    years_no_claims = models.PositiveIntegerField(null=True, blank=True)
    penalty_point = models.PositiveIntegerField(null=True, blank=True)
    pickup_date = models.DateField()
    return_date = models.DateField()
    is_under_25 = models.BooleanField()
    is_child_seat = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    #added to fix error
    year = models.PositiveIntegerField()

    class Meta:
        db_table = 'reservations'
    
    def __str__(self):
        return self.model.model_name
