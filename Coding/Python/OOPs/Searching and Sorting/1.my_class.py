class Car:
    def __init__(self,windows,doors,engine):
        self.windows=windows
        self.doors=doors
        self.engine=engine
    def drive(self):
        print(f"The person will drive {self.engine_type} car.")

Car(4,4,"petrol")

 