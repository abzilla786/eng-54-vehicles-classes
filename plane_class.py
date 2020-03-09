# import my vehicle class
from vehicles_class import *

# define plane class here and make it inherit from vehicle
class plane(vehicles):

    def __init__(self, n_passengers, cargo):
        self.n_passengers = n_passengers
        self.cargo = cargo

    def take_off(selfs):
        return 'take off'
    def touch_down(self):
        return 'we have touched down'
