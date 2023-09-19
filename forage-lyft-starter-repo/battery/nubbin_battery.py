from abc import ABC

from datetime import datetime

import sys
sys.path.append("./forage-lyft-starter-repo")

from car import Car

class NubbinBattery(Car, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
    
    def battery_should_be_serviced(self):
        # Nubbin Battery should be serviced every 4 years
        return self.last_service_date.year - self.current_date.year >= 4