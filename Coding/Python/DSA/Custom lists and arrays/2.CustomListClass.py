import ctypes

class CustomList:
    def __init__(self,):
        initialCapacity=1
        self.capacity=initialCapacity
        self.size=0
        self.array=self.create_array(self.capacity)

        def create_array(self,capacitiy):
            # Create a new referential array with given capacity.
            return (capacitiy*ctypes.py_object)()
