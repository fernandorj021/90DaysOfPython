# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(self.name, self.age)
#
#
# class Student(Person):
#     def __init__(self, name, age, dob):
#         self.sname = name
#         self.sage = age
#         self.dob = dob
#         super().__init__("John", age)
#
#     def displayInfo(self):
#         print(self.sname, self.sage, self.dob)
#
#
#
# obj = Student("Sam", 20, "10-02-2024")
# obj.display()
# obj.displayInfo()

#-----------------------------------------------------------------------------------------------------------------------
# class Parent(object):
#     def display(self):
#         print("I am the Parent Class")
#
#
# class Child(Parent):
#     def child_display(self):
#         print("I am the Child of Parent")
#
#
# obj = Child()
# obj.display()
# obj.child_display()

#-----------------------------------------------------------------------------------------------------------------------
# # Multiple Inheritance
#
# class Father(object):
#     def father_display(self):
#         print("I am the Father Class")
#
#
# class Mother(object):
#     def mother_display(self):
#         print("I am the Mother Class")
#
# class Child(Father, Mother):
#     def child_display(self):
#         print("I am the Child")
#
#
# obj = Child()
# obj.child_display()
# obj.father_display()
# obj.mother_display()

#-----------------------------------------------------------------------------------------------------------------------
# # Multi-level Inheritance#
# class GrandFather(object):
#     def grand_father_display(self):
#         print("I am the Grand Father Class")
#
# class Father(GrandFather):
#     def father_display(self):
#         print("I am the Father Class")
#
# class Child(Father):
#     def child_display(self):
#         print("I am the Child")
#
#
# obj = Child()
# obj.child_display()
# obj.father_display()
# obj.grand_father_display()

#-----------------------------------------------------------------------------------------------------------------------
# Method overloading
class MathOperations:
    def add(self,a,b):
        return a+b

    def add(self,a,b,c):
        return a+b+c

    def add(self,a,b,d):
        return a+b+d

#-----------------------------------------------------------------------------------------------------------------------
# Method overriding
class Father:
    def display(self):
        print("I am the method of the Parent Class")


class Child(Father):
     def display(self):
         print("I am the method of the Child Class")


obj = Child()
obj.display()












