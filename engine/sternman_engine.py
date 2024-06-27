from datetime import date
from engine.engine import Engine

class SternmanEngine(Engine):
    def __init__(self, last_service_date: date, warning_light_is_on: bool):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        return self.warning_light_is_on

