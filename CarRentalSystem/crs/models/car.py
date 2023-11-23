from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from crs.models.reservation import Reservation, Features
from crs.models.factory import car_factory


class Car(models.Model):
    
    
    # Link to a CarModel instance. When the linked CarModel is deleted, this Car instance is also deleted.
    model = models.ForeignKey("crs.CarModel", on_delete=models.CASCADE, related_name='cars')
    # Link to a Reservation instance. It's optional (can be null) and will be set to null if the linked Reservation is deleted.
    reservation = models.ForeignKey("crs.Reservation", on_delete=models.SET_NULL, null=True, related_name='car_reservations')
    year = models.CharField(max_length=4)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    features = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


#sets the table name in the database to 'cars' 
    class Meta:
        db_table = 'cars'

#returns the car's model name for a readable representation
    def __str__(self):
        return self.model.model_name
    
    @property
    def add_price_for_under_25(self):
        if self.reservation.is_under_25:
            return 100
        else:
            return 0

    @property
    def add_price_for_child_seat(self):
        if self.reservation.is_child_seat:
            return 25
        else:
            return 0

#Listens for when a new reservation is made
@receiver(post_save, sender=Reservation)
def create_car_instance(sender, instance, created, **kwargs):
    if created:
        # New car instance is created and initialized with details from the reservation when a new reservation is created 
        car = Car(
            model=instance.model,
            reservation=instance,
            year=instance.model.year,
            price=instance.model.price,
        )
        # call the car factory method
        car_factory(car, instance.model, instance.model.year, instance.model.price)  
