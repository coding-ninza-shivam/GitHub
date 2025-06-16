'''
Encapsulation:
    Wrapping data (variables) and methods (functions) together as a single unit.
    It restricts direct access to some of an object's components, preventing
    accidental interference and misuse of data.
'''

# 1. Public Attributes Example
class Person:
    def __init__(self, name, age):
        self.name = name     # Public
        self.age = age       # Public


# 2. Private Attributes Example
class PrivatePerson:
    def __init__(self, name, age):
        self.__name = name   # Private
        self.__age = age     # Private

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name


'''
Note:
    __name is a private attribute, not accessible directly from outside the class.
    get_name() and set_name() allow controlled access to private attributes.
'''

# 3. Protected Attributes Example
class ProtectedPerson:
    def __init__(self, name, age):
        self._name = name    # Protected
        self._age = age      # Protected

    # Getter method for _name
    def get_name(self):
        return self._name

    # Setter method for _name
    def set_name(self, name):
        self._name = name