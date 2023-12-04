from django.db import models

#Note this class is a copy of the car Model 

LOCATION_CHOICES = (
    ('Dublin', 'Dublin'),
    ('Cork', 'Cork'),
    ('Limerick', 'Limerick'),
)


class Vehicle(models.Model):
    model_name = models.CharField(max_length=255, unique=True)
    year = models.CharField(max_length=4, default='YYYY')
    price = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)
    available_from_date = models.DateField(null=True, default=None)
    available_to_date = models.DateField(null=True, default=None)
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.year} {self.model_name}"
    
    class Meta:
        db_table = 'inventory'
