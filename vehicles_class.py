# define vehicle class here
class vehicles():

    # Characterists:
    # n_passangers
    # size_cargo
    def __init__(self, n_passengers, cargo):
        self.n_passengers = n_passengers
        self.cargo = cargo

    # methods :
    # accelerate
    # brake
    def accelerate(self):
        return 'speeding up'

    def brake(self):
        return 'slowing down'


car = vehicles(5, '500litres')
print(car)

print(car.n_passengers)
print(car.cargo)

print(car.accelerate())
print(car.brake())
