'''
Polmorphism:(One interface, many implementations)
            It allows object of different classes to be treated as object of a common superclass.
            It provide a way to perfoem a single action in different forms.
            It is typically achieved by method overriding and interferences.

        Method Overriding:
                          It allows a child to provide a specific implementation of a method 
                          that is already defined in its parent class.
''' 
######## Polymorphism + Method Overriding #########

#Base class
class Animal:
    def speak(self):
        return "Sound of the animal"

#Derived class 
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
#Derived class 
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
animals = [Animal(), Dog(), Cat() ]
for animal in animals:
    print(animal.speak())

'''
Interference:[Abstract Base Class (ABCs)]
             These are used to define a common method to a group of relatable objects .
             They can enforce that derived classes implement particular methods, promoting
             consistency across different implementations.

'''
######## Polymorphism + Interference #########
from abc import ABC, abstractmethod
# Define ABC 
class vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Deerived class 1
class Car(vehicle):
    def start_engine(self):
        return "Car engine started."
    
# Derived class 2
class Motorcycle(vehicle):
    def start_engine(self):
        return "Motercycle engine started."
    
# Polymorphic behavior
vehicles = [Car(), Motorcycle()]
for v in vehicles:
    print(v.start_engine())