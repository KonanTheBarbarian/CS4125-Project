from .vehBuilder import VehicleBuilder
from crs.models.vehicle import Vehicle 

class ConcreteVehicleBuilder(VehicleBuilder):
    def __init__(self):
        self.vehicle = Vehicle()

    def build_model_name(self, model_name):
        self.vehicle.model_name = model_name
        return self

    def build_year(self, year):
        self.vehicle.year = year
        return self

    def build_price(self, price):
        self.vehicle.price = price
        return self

    def build_available_from_date(self, available_from_date):
        self.vehicle.available_from_date = available_from_date
        return self

    def build_available_to_date(self, available_to_date):
        self.vehicle.available_to_date = available_to_date
        return self

    def build_location(self, location):
        self.vehicle.location = location
        return self

    def get_result(self):
        return {
            'model_name': self.vehicle.model_name,
            'year': self.vehicle.year,
            'price': self.vehicle.price,
            'available_from_date': self.vehicle.available_from_date,
            'available_to_date': self.vehicle.available_to_date,
            'location': self.vehicle.location,
        }


    """
    def get_result(self):
        return {
            'make': self.vehicle.make,
            'model': self.vehicle.model,
            'year': self.vehicle.year,
            'color': self.vehicle.color,
            'price': self.vehicle.price,
        }
    """