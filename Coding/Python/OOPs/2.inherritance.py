class Car:
    def __init__(self,windows,doors,engine):
        self.windows=windows
        self.doors=doors
        self.engine=engine
    def drive(self):
        print(f"The person will drive {self.engine_type} car.")

Car(4,4,"petrol")


#### single inheritance
class Tesla(Car):
    def __init__(self, windows, doors, engine, is_self_driving):
        super().__init__(windows, doors, engine)
        self.is_self_driving=is_self_driving

#### multiple inheritance

# base class 1
class Animal:
    def __init__(self,name):
        self.name=name

# base class 2
class Pet:
    def __init__(self, owner):
        self.owner=owner

# Derived class
class Dog(Animal,Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)


Dog("Sheru","Ramu")