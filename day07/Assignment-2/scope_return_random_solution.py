import math
import random

global_var = 10
counter  = 0

def local_scope_example():
    '''
    global_var is defined outside the function, so it's a global variable — accessible anywhere inside the same module,
    including inside functions.

    local_var is defined inside the function, so it's a local variable — only accessible within local_scope_example()
    '''

    local_var = 1
    print(global_var, local_var)

local_scope_example() # Output: 10, 1


def calculate_square(num):
    return math.sqrt(num)

print(calculate_square(4))  # Output: 2.0
print(calculate_square(5))  # Output: 2.23606797749979
print(calculate_square(16)) # Output: 4.0


def generate_random_number():
    random_number = random.randint(1,100)
    print(random_number * 2)

generate_random_number()

def increment_counter():
    global counter
    counter = counter + 1
    return counter

print(increment_counter()) # Output: 1
print(increment_counter()) # Output: 2
print(increment_counter()) # Output: 3


def calculate_area(length, width):
    return length * width

print(calculate_area(8, 5))  # Output: 40
print(calculate_area(4, 12))  # Output: 48
print(calculate_area(2,5))  # Output: 10