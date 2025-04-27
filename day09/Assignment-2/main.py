def check_category(rating,budget_in_millions):
    if rating >=8 and budget_in_millions >= 100:
        return "Blockbuster"
    elif rating >=8 and budget_in_millions < 100:
        return "Hit"
    else:
        return "Flop"

print(check_category(8.5, 120))
print(check_category(8.2, 80))
print(check_category(7.9, 150))


def is_eligible(age, valid_registration):
    if age >= 18 and valid_registration:
        return True

    return False

eligible = is_eligible(17, True)
if eligible:
    print("Is eligible.")
else:
    print("Is not eligible.")



def check_type_of_triangle(length1, length2, length3):
    if length1 == length2 and length1 == length3:
        print("equilateral")
    elif ((length1 == length2 and length1 != length3) or (length2 == length3 and length2 != length1)
          or (length3 == length1 and length3 != length2 )):
        print("Isosceles")
    else:
        print("Scalene")

check_type_of_triangle(5, 5, 5)   # equilateral
check_type_of_triangle(5, 5, 3)   # isosceles
check_type_of_triangle(5, 4, 3)   # scalene



def calculate_shipping_cost(weight, is_international):
    if weight > 10 and is_international:
        return "$100"
    elif weight > 10 and (not is_international):
        return "$60"
    elif weight <= 10 and is_international:
        return "$70"
    else:
        return "$40"

print(calculate_shipping_cost(12, True))   # $100
print(calculate_shipping_cost(12, False))  # $60
print(calculate_shipping_cost(8, True))    # $70
print(calculate_shipping_cost(8, False))   # $40











