from django.core.management.base import BaseCommand
from crs.models.reservation import CarModel
from crs.models.vehicle import Vehicle
class Command(BaseCommand):
    help = 'Copy data from CarModel to Vehicle'

    def handle(self, *args, **options):
        # Retrieve data from CarModel
        car_models = CarModel.objects.all()

        # Copy data to Vehicle
        for car_model in car_models:
            Vehicle.objects.create(
                model_name=car_model.model_name,
                year=car_model.year,
                price=car_model.price,
                available_from_date=car_model.available_from_date,
                available_to_date=car_model.available_to_date,
                location=car_model.location,
                created_at=car_model.created_at,
            )

        self.stdout.write(self.style.SUCCESS('Data copied successfully'))