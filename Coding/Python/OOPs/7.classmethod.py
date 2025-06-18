class IITPatna:
    course = 'DSA'
    list_of_instances = []

    def __init__(self, name):
        self.name = name
        IITPatna.list_of_instances.append(self)

    @classmethod
    def get_course(cls):
        return f"Course: {cls.course}"

    @classmethod
    def get_instance_count(cls):
        return f"Number of instances: {len(cls.list_of_instances)}"

    @staticmethod
    def welcome_message():
        return "Welcome to IIT Patna!"

# Creating instances
g1 = IITPatna('Alice')
g2 = IITPatna('Bob')

# Calling class methods
print(IITPatna.get_course())  
print(IITPatna.get_instance_count())  

# Calling static method
print(IITPatna.welcome_message())