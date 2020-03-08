# import my vehicle class
from vehicles_class import *

# define car class here and make it inherit from vehicle
class car(vehicles):
    #Characterists:
    # brand
    # horse_power
    # max_speed
    def __init__(self, n_passengers, cargo, brand, horse_power, max_speed):
        super().__init__(n_passengers, cargo)
        self.brand = brand
        self.horse_power = horse_power
        self.max_speed = max_speed
#methods :
# park
# honk
    def park(self):
        return 'car parked'
    def honk(self):
        return 'BEEEEEEPPPPPP BBEEEPPPPP'


