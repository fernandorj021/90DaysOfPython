class test:
    @staticmethod
    def square(x):
        test.result = x*x


t1 = test()
t2 = test()

t1.square(2)
print(t1.result)

#-----------------------------------------------------------------------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 25)
print(p1.name)
print(p1.age)

#-----------------------------------------------------------------------------------------------------------------------
# Doc Strings
def multiply(a, b):
    """Multiplies two number and return the result
    Args:
         a(int) : The first number
         b(int) : The second number

    Returns:
        int : The product of a and b"""

    return a*b

print(multiply.__doc__)
help(multiply)

#-----------------------------------------------------------------------------------------------------------------------
# Doc Strings in classes
class ComplexNumber:
    """
    This is a class for mathematical operations on complex numbers

    Attributes:
        real(int): The real part of the complex number
        imag(int): The imaginary part of the complex number
    """

    def __init__(self, real, imag):
        """
        The constructor for complexNumber Class
        :param real: The real part value
        :param imag: The imag part value
        """

        self.real = real
        self.imag = imag

    def add(self, num):
        """
        The function to add the two complex numbers
        :param num: The complex number to be added
        :return: A complex number which contains the sum
        """

        re = self.real+num.real
        im = self.imag+num.imag

        return ComplexNumber(re, im)

help(ComplexNumber)
help(ComplexNumber.add)

#-----------------------------------------------------------------------------------------------------------------------
print("Hello")

def main():
    print("Hey there")

if __name__ =="__main__":
    main()









