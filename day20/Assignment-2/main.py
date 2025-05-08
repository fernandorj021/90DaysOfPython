# 1
# class Vehicle:
#
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
#
# class Bus(Vehicle):
#     def __init__(self, name, mileage, capacity):
#         super().__init__(name,mileage, capacity)
#
#     def fare(self):
#         base_fare = super().fare()
#         return base_fare + (0.10 * base_fare)
#
#
#
# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())

#-----------------------------------------------------------------------------------------------------------------------
# 2
# def check_class(the_object):
#     return type(the_object)
#
# print(check_class(School_bus))

#-----------------------------------------------------------------------------------------------------------------------
# 3
class Vehicle:

    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)


def check_instance_of_vehicle(the_object):
    return isinstance(the_object, Vehicle)

print(check_instance_of_vehicle(School_bus))









