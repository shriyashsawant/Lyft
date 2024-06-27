from datetime import date
from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery
from tire.specific_tire_model import SpecificTireModel
from car import Car

class Thovex(Car):
    def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int, current_date: date, wear_tear: float):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tires = SpecificTireModel(wear_tear)
        super().__init__(engine, battery, tires)
