# Global Variables
global_var = 10

def func():
    print("Global variable inside function:", global_var)

func()  # Output: Global variable inside function: 10

# Local Variables
def func():
    local_var = 20
    print("Local variable inside function:", local_var)

func()  # Output: Local variable inside function: 20

# Global vs. Local Variables
global_var = 10

def func():
    local_var = 20
    print("Global variable:", global_var)
    print("Local variable:", local_var)


func()  # Output: Global variable: 10, Local variable: 20

# Accessing Global Variables from within Functions
global_var = 10

def func():
    global global_var
    global_var = 30
    print("Modified global variable inside function:", global_var)


func()  # Output: Modified global variable inside function: 30

# Nested Functions and Variable Scope
'''
In Python, nested functions can access variables from outer functions (closure). 
However, if a variable with the same name is declared within the inner function, 
it creates a new local variable with the same name, shadowing the outer variable
'''
def outer_func():
    outer_var = 10

    def inner_func():
        inner_var = 20
        print("Inner variable:", inner_var)  # Accessing inner variable
        print("Outer variable:", outer_var)  # Accessing outer variable

    inner_func()


outer_func()  # Output: Inner variable: 20, Outer variable: 10

import random

random_number = random.randint(1,10)
print(random_number)

random_number = random.random()
print(random_number)

my_list = [1,2,3,4,5]
random_number = random.choice(my_list)
print(random_number)

my_list = ["red", "blue", "ping", "mind"]
random_number = random.choice(my_list)
print(random_number)

my_list = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(my_list)
print(my_list)

my_list = [1,2,3,4,5,6,7,8,9,10]
random_sample = random.sample(my_list, 3)
print(random_sample)


import math
print(math.sqrt(4))
print(math.fabs(-8))
print(math.factorial(5))
print(math.log(2,3))
print(math.log2(3))
print(math.pow(3,2))
print(math.gcd(30,20))
print(math.sin(30))
print(math.cos(30))


