from datetime import date
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class CarFactory:
    @staticmethod
    def create_calliope(last_service_date: date, current_mileage: int, last_service_mileage: int, current_date: date, wear_tear: float) -> Calliope:
        return Calliope(last_service_date, current_mileage, last_service_mileage, current_date, wear_tear)

    @staticmethod
    def create_glissade(last_service_date: date, current_mileage: int, last_service_mileage: int, current_date: date, wear_tear: float) -> Glissade:
        return Glissade(last_service_date, current_mileage, last_service_mileage, current_date, wear_tear)

    @staticmethod
    def create_palindrome(last_service_date: date, warning_light_is_on: bool, current_date: date, wear_tear: float) -> Palindrome:
        return Palindrome(last_service_date, warning_light_is_on, current_date, wear_tear)

    @staticmethod
    def create_rorschach(last_service_date: date, current_mileage: int, last_service_mileage: int, current_date: date, wear_tear: float) -> Rorschach:
        return Rorschach(last_service_date, current_mileage, last_service_mileage, current_date, wear_tear)

    @staticmethod
    def create_thovex(last_service_date: date, current_mileage: int, last_service_mileage: int, current_date: date, wear_tear: float) -> Thovex:
        return Thovex(last_service_date, current_mileage, last_service_mileage, current_date, wear_tear)
