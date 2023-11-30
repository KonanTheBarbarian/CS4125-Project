from .vehBuilder import VehicleBuilder

class VehicleDirector:
    def __init__(self, builder: VehicleBuilder):
        self.builder = builder

    def construct(self, model_name, year, price, available_from_date, available_to_date, location):
        return (
            self.builder
            .build_model_name(model_name)
            .build_year(year)
            .build_price(price)
            .build_available_from_date(available_from_date)
            .build_available_to_date(available_to_date)
            .build_location(location)
        )