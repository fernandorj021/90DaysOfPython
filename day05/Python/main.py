def addition(n1, n2):
    result = n1 + n2
    print(f"The sum of {n1} and {n2} is {result}")

def subtraction(n1, n2):
    result = n1 - n2
    print(f"The subtraction of {n1} and {n2} is {result}")

def multiplication(n1, n2):
    result = n1 * n2
    print(f"The multiplication of {n1} and {n2} is {result}")


def division(n1, n2):
    result = n1 / n2
    print(f"The division of {n1} and {n2} is {result}")


addition(10,2)
subtraction(10,2)
multiplication(10,2)
division(10,2)

def greeting(msg="Good morning", name="Will"):
    print(f"{msg} {name}")

greeting("Hello", "Fernando")
greeting()

def calculate_area(length, width):
    print(length)
    print(width)
    print(f"The area is {length*width}")

calculate_area(width=1, length=2)