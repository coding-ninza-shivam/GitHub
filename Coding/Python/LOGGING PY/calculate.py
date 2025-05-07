"""Single user configuration"""

# import logging
# import employees

# logging.basicConfig(filename='Sample.log',filemode='w',format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)

# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b
# def multiply(a, b):
#     return a * b
# def divide( a, b):
#     if b == 0:
#         return "Error: Division by zero"
#     return a / b

# num1= 10
# num2= 5

# add_result= add(num1, num2)
# logging.debug('Add: {} + {} = {}'.format(num1, num2, add_result))
# sub_result= subtract(num1, num2)
# logging.debug('Sub: {} - {} = {}'.format(num1, num2, sub_result))
# mul_result= multiply(num1, num2)
# logging.debug('Mul: {} * {} = {}'.format(num1, num2, mul_result))
# div_result= divide(num1, num2)
# logging.debug('Div: {} / {} = {}'.format(num1, num2, div_result))

"""Multi user configuration"""


import logging
import employees


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('Calculat.log')
# file_handler.setLevel(logging.ERROR)
''' if we want to set the level of our file handler'''
file_handler.setFormatter(formatter)

'''
If we want to see the debug statements to display to the console 
so we will create a stream handler in spite of a file handler
'''

stream_handler = logging.StreamHandler( )
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide( a, b):
    try:
        result= a / b
    except ZeroDivisionError:
        logger.error("Tried to divide by zero")
    else:
        return result

num1= 10
num2= 5

add_result= add(num1, num2)
logger.debug('Add: {} + {} = {}'.format(num1, num2, add_result))
sub_result= subtract(num1, num2)
logger.debug('Sub: {} - {} = {}'.format(num1, num2, sub_result))
mul_result= multiply(num1, num2)
logger.debug('Mul: {} * {} = {}'.format(num1, num2, mul_result))
div_result= divide(num1, num2)
logger.debug('Div: {} / {} = {}'.format(num1, num2, div_result))

