#-----------------------------------------------------------------------------------------------------------------------
# Encapsulation
# class Student:
#     def __init__(self, name, rank):
#         self.name = name
#         self.rank = rank
#
#     def demofunc(self):
#         print(f"I am {self.name}")
#         print(f"I got rank {self.rank}")
#
#
# st1 = Student("Steve", 1)
# st2 = Student("Cris", 2)
# st3 = Student("Mark", 3)
# st4 = Student("Kate", 4)
#
# st1.demofunc()
# st2.demofunc()
# st3.demofunc()
# st4.demofunc()

#-----------------------------------------------------------------------------------------------------------------------
# # Access Modifiers - private
# class Student:
#     def __init__(self, name, rank):
#         self.name = name
#         self.__rank = rank
#
#     def demofunc(self):
#         print(f"I am {self.name}")
#         print(f"I got rank {self.__rank}")
#
#
# st1 = Student("Steve", 1)
#
# print(st1.name)
#
# # AttributeError: 'Student' object has no attribute '__rank'
# print(st1.__rank)
#
# st1.demofunc()

#-----------------------------------------------------------------------------------------------------------------------
# # Access Modifiers - protected
# class Animal:
#     def __init__(self, name):
#         self._name = name  # protected attribute
#
#     def _make_sound(self):  # protected method
#         print("Generic animal sound")
#
#
# class Dog(Animal):
#     def bark(self):
#         print(f"{self._name} says: Woof woof!")  # accessing protected attribute
#         self._make_sound()  # accessing protected method
#
#
#
# user_name = input("Enter your dog's name: ")
# my_dog = Dog(user_name)
# my_dog.bark()
# my_dog._make_sound() # Emits warning - Access to a protected member

#-----------------------------------------------------------------------------------------------------------------------
# # Abstract Base Class
# import abc
#
# class Shape(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def area(self):
#         print("hey")
#
# class Retangle(Shape):
#     def __init__(self, x, y):
#         self.l = x
#         self.b = y
#
#     def area(self):
#         return self.l * self.b
#
# r = Retangle(10,20)
# print(f"area: {r.area()}")
#
# s=Shape() # TypeError: Can't instantiate abstract class Shape without an implementation for abstract method 'area'
# s.area()

#-----------------------------------------------------------------------------------------------------------------------
# # Class and Instance Method
# class Employee:
#
#     salary = 25000
#     def __init__(self, name, department):
#         self.name = name
#         self.department = department
#
#     def show(self):
#         print(f"Name: {self.name} Department: {self.department} Salary: {Employee.salary}")
#
#     @classmethod
#     def change_salary(cls, salary):
#         Employee.salary = salary
#
# obj = Employee("John", "Marketing")
# obj.show()
# obj.department = "IT"
# obj.show()
#
# Employee.change_salary(30000)
# print(Employee.salary)
# obj.show()
#
# obj.change_salary(345000)
# obj.show()

#-----------------------------------------------------------------------------------------------------------------------
# Static Methods
class Employee:
    @staticmethod
    def show(x):
        print(f"Inside static method {x*x}")


obj = Employee()
obj.show(2)
Employee.show(4)














