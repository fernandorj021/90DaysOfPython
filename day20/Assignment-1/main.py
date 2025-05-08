# 1
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

#-----------------------------------------------------------------------------------------------------------------------
# 2
# class Vehicle:
#     pass

#-----------------------------------------------------------------------------------------------------------------------
# 3
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#
#     def __init__(self, max_speed, mileage):
#         super().__init__(max_speed,mileage)

#-----------------------------------------------------------------------------------------------------------------------
# 4
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     def __init__(self, max_speed, mileage):
#         super().__init__(max_speed, mileage)
#
#     def seating_capacity(self, capacity=50):
#         return f"The seating capacity of the bus is {capacity} passengers"
#
# bus = Bus(120, 15000)
# print(bus.seating_capacity())
# print(bus.seating_capacity(60))

#-----------------------------------------------------------------------------------------------------------------------
# 5
class Vehicle:
   color = "white"
   def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage


class Bus(Vehicle):
     pass


class Car(Vehicle):
     pass


bus = Bus("School Bus", 80, 15000)
car = Car("Sedan", 120, 10000)

print(bus.color)
print(car.color)
print(Bus.color)
print(Car.color)









