from abc import ABC

from datetime import datetime

import sys
sys.path.append("./forage-lyft-starter-repo")

from car import Car

class SpindlerBattery(Car, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
    
    def battery_should_be_serviced(self):
        # this is the older version of the spindler battery service
        # new Spindler battery requirement changes to 3 years per service
        # service_theshold_date = self.last_service_date.replace(year=self.last_service_date.year+3)
        return self.last_service_date.year - self.current_date.year >= 3
