# def table4(n):
#     result = n*4
#     yield result
#
# a = table4(3)
# print(a.__next__())

#----------------------------------------------------------------------------------------------------------------------
# def table4(n):
#     result1 = n * 4
#     result2 = n * 5
#     result3 = n * 6
#     yield result1
#     yield result2
#     yield result3
#
# a = table4(3)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

#----------------------------------------------------------------------------------------------------------------------
def natural_no(n):
    for i in range(1,n):
     yield i

n = natural_no(10)
print(next(n))
print(next(n))
print(next(n))

#----------------------------------------------------------------------------------------------------------------------





