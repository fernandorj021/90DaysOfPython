try:
    age = int(input("Enter your age: "))
    if age < 18:
        print("You are a teenager")

except:
    print("Please input an integer value")

#-----------------------------------------------------------------------------------------------------------------------
try:
    a = int(input("Enter the first Value: "))
    b = int(input("Enter the second Value: "))
    print(f"Result: {a/b}")

except ValueError:
    print("You need to provide both integer values")
except ZeroDivisionError:
    print("Zero division error")
except:
    print("Unknown error has occurred: please try again...")

#-----------------------------------------------------------------------------------------------------------------------
try:
    age = int(input("Enter your age: "))

except ValueError:
    print("You need to provide a integer value")

else:
    print(f"You are {age} years old")
    if age <= 35:
        print("Young enough to football")
    else:
        print("You are not young enough to football")

#-----------------------------------------------------------------------------------------------------------------------
try:
    age = int(input("Enter your age: "))

except ValueError:
    print("You need to provide a integer value")

else:
    print(f"You are {age} years old")
    if age <= 35:
        print("Young enough to football")
    else:
        print("You are not young enough to football")

finally:
    print("Thanks for providing your information.")

#-----------------------------------------------------------------------------------------------------------------------
while 1:

    try:
        age = int(input("Enter your age: "))

    except ValueError:
        print("You need to provide a integer value")

    else:
        print(f"You are {age} years old")
        if age <= 35:
            print("Young enough to football")
        else:
            print("You are not young enough to football")
        break

    finally:
        print("Thanks for providing your information.")

#-----------------------------------------------------------------------------------------------------------------------

x = int(input("Enter any positive number: "))

if x < 0:
    raise Exception("Expecting positive value!")
else:
    print(x)

#-----------------------------------------------------------------------------------------------------------------------
try:

    x = int(input("Enter any positive number: "))

    if x < 0:
        raise ValueError
except ValueError:
    print("You need to supply a positive number")




























