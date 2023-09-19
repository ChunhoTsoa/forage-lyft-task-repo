from datetime import datetime

import sys
sys.path.append("./forage-lyft-starter-repo")

from engine.sternman_engine import SternmanEngine

from battery.nubbin_battery import NubbinBattery

class Palindrome(SternmanEngine, NubbinBattery):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date, warning_light_is_on)
        
    def needs_service(self):
        # implement NubbinBattery Battery into Palidrome
        # use new battery class
        # if one of these, is true, then return true for need to service the car. 
        # after need to label engine or battery which meets the certiria for service
        if self.engine_should_be_serviced() or self.battery_should_be_serviced():
            return True
        else:
            return False