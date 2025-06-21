import ctypes

class CustomList:
    def __init__(self,):
        initialCapacity=1
        self.capacity=initialCapacity
        self.size=0
        self.array=self.__create_array(self.capacity)

        def __create_array(self,capacity):
            # Create a new referential array with given capacity.
            return (capacity*ctypes.py_object)()
        
        def __resize(self,newCapacity):
            newArray=self.__create_array(newCapacity)
            for i in range(self.size):
                newArray[i]=self.array[i]

            self.array=newArray #Replace the old array
            self.capacity=newCapacity   

        def append(self,item):
            if (self.capacity==self.size):
                self.__resize(2*self.capacity)

            self.array[self.size]=item
            self.size+=1

        def __len__(self):
            return self.size
        
        def __str__(self): # Ex: print(mylist)
            output=""
            for i in range(self.size):
                output = output + str(self.array[i]) + ","
            return "[" + output[:-1] + "]"
        
        def pop(self):
            if (self.size==0):
                return 'IndexError: pop from empty list'
            poppeditem = self.array[self.size-1]
            self.size=self.size-1
            return poppeditem
        
        def __getitem__(self,index):  # EX: myitem[1]
            if (index>=0 and index<self.size):
                return self.array[index]
            else:
                return 'IndexError: index out of range '
             
        def clear(self):  # It does not removes the elements, it reinitialises the string.
            self.size=0

        def insert(self,position,element): # Position will be inside only.
            if (self.capacity==self.size):
                self.__resize(2*self.capacity)
            for index in range(self.size,position,-1):
                self.array[index]=self.array[index-1]
            self.array[position]=element
            self.size+=1

    def remove(self,element):
        found=False
        for position  in range(0,self.size):
            if self.array[position]==element:
                found=True 
                break
        if not found:
            raise ValueError("list.remove(x): x not in list")
        for index in range(position, self.size - 1):
            self.array[index]=self.array[index+1]
        self.size-=1

myList=CustomList()
myList.append(1)
myList.append(2)
print(myList)
print(myList.pop())
print(myList) 
print(myList.pop())
print(myList) 
print(myList.pop())
print(myList) 