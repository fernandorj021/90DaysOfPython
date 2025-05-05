
try:
    age = int(input("Enter your age: "))

except ValueError:
    print("You need to provide a numeric value.")

else:
    if age < 0 or age > 120:
        raise Exception("InvalidAgeError")
    else:
        print(f"Your age is {age}")

#-----------------------------------------------------------------------------------------------------------------------
def divide_numbers(number1, number2):
    try:
        return number1/number2
    except ZeroDivisionError:
        return "Division by zero not allowed!"

print(divide_numbers(4,2))
print(divide_numbers(35,5))
print(divide_numbers(4,0))

#-----------------------------------------------------------------------------------------------------------------------

try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    print(f"First Number: {first_number} and Second Number: {second_number}")
except:
    print("You need to provide both integer values")

finally:
    print("Thanks for use this app!")

#-----------------------------------------------------------------------------------------------------------------------
import math
try:
    number_to_square_root = int(input("Enter a number: "))
    if number_to_square_root < 0:
        raise ValueError
except ValueError:
    print("Enter a non negative number.")
else:
    print(f"Square root of {number_to_square_root} is {math.sqrt(number_to_square_root)}")












