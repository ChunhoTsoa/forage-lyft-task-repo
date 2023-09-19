import sys
sys.path.append("./forage-lyft-starter-repo")

class CarriganTire():
    def __init__(self, tires_condition):
        self.tires_condition = tires_condition
        
    def tires_should_be_serviced(self):
        # Carrigan tires should be serviced only when one or 
        # more of the values in the tire wear array is greater than or equal to 0.9.
        sum = 0
        for x in range(len(self.tires_condition)):
            sum += self.tires_condition[x]
        return (sum / 4) < 0.9