from django.db import models


class Car(models.Model):
    model = models.ForeignKey("crs.CarModel", on_delete=models.CASCADE, related_name='cars')
    reservation = models.ForeignKey("crs.Reservation", on_delete=models.SET_NULL, null=True, related_name='car_reservations')
    year = models.CharField(max_length=4)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    features = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cars'

    def __str__(self):
        return self.model.model_name

# The base decorator class that wraps a Car object
class CarDecorator:
    def __init__(self, car):
        self._car = car

 #allows the decorator to act like a Car object.
    def __getattr__(self, attr): 
        return getattr(self._car, attr)

    def get_price(self):
        return self._car.price

# Concrete decorators extend the behavior of Car objects
class Under25Decorator(CarDecorator):
    def get_price(self):
        base_price = super().get_price()
        return base_price + 100 if self._car.reservation and self._car.reservation.is_under_25 else base_price

class ChildSeatDecorator(CarDecorator):
    def get_price(self):
        base_price = super().get_price()
        return base_price + 25 if self._car.reservation and self._car.reservation.is_child_seat else base_price

# Example usage:
# car = Car.objects.get(id=1) # Get the car instance from the database
# decorated_car = Under25Decorator(car)
# final_price = decorated_car.get_price()
