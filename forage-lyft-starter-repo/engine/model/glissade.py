from datetime import datetime

import sys
sys.path.append("./forage-lyft-starter-repo")

from engine.willoughby_engine import WilloughbyEngine

from battery.spindler_battery import SpindlerBattery

class Glissade(WilloughbyEngine, SpindlerBattery):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date, current_mileage, last_service_mileage)
        
    def needs_service(self):
        # implement spindler Battery into Glissade
        # use new battery class
        # if one of these, is true, then return true for need to service the car. 
        # after need to label engine or battery which meets the certiria for service
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
