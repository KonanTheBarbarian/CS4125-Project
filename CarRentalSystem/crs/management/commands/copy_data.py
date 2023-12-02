from django.core.management.base import BaseCommand
from crs.models.reservation import CarModel
from crs.models.vehicle import Vehicle
class Command(BaseCommand):
    help = 'Copy data from Vehicle to CarModel'

    def handle(self, *args, **options):
        # Retrieve data from Vehicle
        vehicles = Vehicle.objects.all()

        # Copy data to CarModel
        for vehicle in vehicles:
            CarModel.objects.create(
                model_name=vehicle.model_name,
                year=vehicle.year,
                price=vehicle.price,
                available_from_date=vehicle.available_from_date,
                available_to_date=vehicle.available_to_date,
                location=vehicle.location,
                created_at=vehicle.created_at,
            )

        self.stdout.write(self.style.SUCCESS('Data copied successfully'))