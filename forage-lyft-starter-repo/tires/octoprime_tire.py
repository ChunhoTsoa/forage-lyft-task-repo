import sys
sys.path.append("./forage-lyft-starter-repo")
# might need to implement Car abstract class for later update
class OctoprimeTire():
    def __init__(self, tires_condition):
        self.tires_condition = tires_condition
        
    def tires_should_be_serviced(self):
        # Octoprime tires should be serviced only 
        # when the sum of all values in the tire wear array is greater than or equal to 3.
        sum = 0
        for x in range(len(self.tires_condition)):
            sum += self.tires_condition[x]
        return sum < 3