def is_divisible_by_6(number):
    return number%6 == 0


num = int(input("Enter a number: "))

is_divisible = is_divisible_by_6(num)

if is_divisible:
    print(f"{num} is divisible by 6.")
else:
    print(f"{num} is not divisible by 6")



def grade_category(grade):
    if grade >= 90 and grade <= 100:
        return "A"
    elif grade >= 80 and grade <= 89:
        return "B"
    elif grade >= 70 and grade <= 79:
        return "C"
    elif grade >= 60 and grade <= 69:
        return "D"
    elif grade >= 0 and grade <= 59:
        return "F"
    else:
        return "Invalid grade."


print(grade_category(91))
print(grade_category(100))
print(grade_category(80))
print(grade_category(82))
print(grade_category(0))
print(grade_category(5))
print(grade_category(59))
print(grade_category(101))
print(grade_category(-1))


def is_leap_year(year):
    if year%4 == 0 and (not year%100 == 0 or year%400 == 0):
        return True
    else:
        return  False


print(is_leap_year(1996))
print(is_leap_year(1900))
print(is_leap_year(2000))
print(is_leap_year(2023))
print(is_leap_year(2400))


def largest_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


print(largest_number(1,2,3))
print(largest_number(4,5,1))
print(largest_number(6,5,1))