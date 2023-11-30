from abc import ABC, abstractmethod

class VehicleBuilder(ABC):
    @abstractmethod
    def build_model_name(self, model_name):
        pass

    @abstractmethod
    def build_year(self, year):
        pass

    @abstractmethod
    def build_price(self, price):
        pass

    @abstractmethod
    def build_available_from_date(self, available_from_date):
        pass

    @abstractmethod
    def build_available_to_date(self, available_to_date):
        pass

    @abstractmethod
    def build_location(self, location):
        pass

    @abstractmethod
    def get_result(self):
        pass
        pass