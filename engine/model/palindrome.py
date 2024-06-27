from datetime import date
from engine.sternman_engine import SternmanEngine
from tire.specific_tire_model import SpecificTireModel
from battery.spindler_battery import SpindlerBattery
from car import Car

class Palindrome(Car):
    def __init__(self, last_service_date: date, warning_light_is_on: bool, current_date: date, wear_tear: float):
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        battery = SpindlerBattery(last_service_date)
        tires = SpecificTireModel(wear_tear)
        super().__init__(engine, battery, tires)
