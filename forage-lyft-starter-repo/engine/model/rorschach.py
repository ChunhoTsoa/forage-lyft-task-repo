from datetime import datetime


import sys
sys.path.append("./forage-lyft-starter-repo")

from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery


class Rorschach(WilloughbyEngine, NubbinBattery):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, current_mileage, last_service_mileage)
        
    def needs_service(self):
        # implement NubbinBattery Battery into Rorschach
        # use new battery class
        # if one of these, is true, then return true for need to service the car. 
        # after need to label engine or battery which meets the certiria for service
        if self.engine_should_be_serviced() or self.battery_should_be_serviced():
            return True
        else:
            return False
        
