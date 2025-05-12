# from threading import Thread
#
# def swap_number():
#     print("The thread has been started")
#     a=5
#     b=6
#     print("Numbers before swapping are ",a, " and ", b)
#     temp = a
#     a=b
#     b=temp
#     print("Numbers after swapping are ", a, " and ", b)
#
# t1 = Thread(target=swap_number)
# t1.start()

#-----------------------------------------------------------------------------------------------------------------------
# from threading import Thread
#
# def swap_number(a,b):
#     print("The thread has been started")
#     print("Numbers before swapping are ",a, " and ", b)
#     temp = a
#     a=b
#     b=temp
#     print("Numbers after swapping are ", a, " and ", b)
#
# t1 = Thread(target=swap_number,args=[5,6])
# t1.start()

#-----------------------------------------------------------------------------------------------------------------------
# from threading import Thread
# import threading
#
# class Natural(Thread):
#
#     def run(self):
#         print(threading.current_thread().name)
#         for x in range(1,11):
#             print(x)
#
#
# obj = Natural()
# obj.run()

#-----------------------------------------------------------------------------------------------------------------------
# from threading import Thread
# import threading
#
# class Natural:
#
#     def numbers(self):
#         print(threading.current_thread().name)
#         for x in range(1,11):
#             print(x)
#
# print(threading.current_thread().name)
# obj = Natural()
# t1 = Thread(target=obj.numbers)
# t1.start()

#-----------------------------------------------------------------------------------------------------------------------
from threading import Thread
import threading

def NaturalNo():
    print(threading.current_thread().name, " has been started" )
    for x in range(1,10):
        print(x)

    print(threading.current_thread().name, " has ended")

t1 = Thread(target=NaturalNo)
t2 = Thread(target=NaturalNo)

t1.start()
t2.start()













