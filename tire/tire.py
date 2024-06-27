from abc import ABC, abstractmethod
from car import Serviceable

class Tire(Serviceable, ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

