# import all the classes
import self as self

from vehicles_class import *
import car_class
import plane_class

# create 2 vehicle instances
vehicle = vehicles(6, '500litres')
vehicle2 = vehicles(5, '350litres')

# call methods and attributes to test
print(vehicle.cargo)
print(vehicle.n_passengers)
print(vehicle.accelerate())
print(vehicle.brake())

print(vehicle2.cargo)
print(vehicle2.n_passengers)
print(vehicle2.accelerate())
print(vehicle2.brake())

# create 2 car instances
car1 = car_class.car(5, '300litres', 'BMW', '450bhp', 210)
car2 = car_class.car(2, '150litre', 'Nissan', '350bhp', 190)

# make car accelerate and make them break
print(car_class.car.accelerate(self))
print(car_class.car.brake(self))

# make car honk and park
print(car_class.car.honk(self))
print(car_class.car.park(self))

# create 2 plane instances here
plane1 = plane_class.plane(650, '1000litres')
plane2 = plane_class.plane(400, '500litres')

# make plane accelerate and make them break
print(plane_class.plane.accelerate(self))
print(plane_class.plane.brake(self))

# make plane fly and land
print(plane_class.plane.take_off(self))
print(plane_class.plane.touch_down(self))
