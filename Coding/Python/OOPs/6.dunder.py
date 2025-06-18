class String:
    # magic method to initiate object
    def __init__(self, string):
        self.string = string     
    # print our string object
    def __repr__(self):
        return 'Object: {}'.format(self.string)
    # magic method for string concatenation   
    def __add__(self, other):
        return self.string + other

if __name__ == '__main__':
    string1 = String('Hello')
    print(string1 +' Geeks')