'''
Abstraction:
    The process of hiding the complex implementation details and showing only the necassary features of an object.
    This helps in reducing programming complexity and effort.
'''

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    def drive(self):
        print("The vehical can be drived.")

    @abstractmethod
    def start_engine(self):
        print("The engine got started.")

## Here car can use drive method but to use the start_engine method we have to define our own function.

# Child class
class Car(Vehicle):
    def start_engine(self):
        print("The engine got started.")

def operate_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.drive()

car=Car()
operate_vehicle(car)
