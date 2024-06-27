from tire.tire import Tire

class SpecificTireModel(Tire):
    def __init__(self, wear_tear: float):
        self.wear_tear = wear_tear

    def needs_service(self) -> bool:
        return self.wear_tear > 0.8
