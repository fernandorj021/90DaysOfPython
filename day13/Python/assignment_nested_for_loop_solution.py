for number in range(1,6):
    for multiplier in range(0,11):
        print(f"{number} x {multiplier} = {number * multiplier}")
    print()

#----------------------------------------------------------------------------------------------------------------------
n = int(input("Enter a number: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#----------------------------------------------------------------------------------------------------------------------

first = 0
second = 0
result = 0
for i in range(0, 1):
    for j in range(1, 12):
        if j == 1:
            first = i
            print(f"{first}", end=" ")
            second = j
            print(f"{second}", end=" ")
            result = first + second
            print(f"{result}", end=" ")
        else:
            first = second
            second = result
            result = first + second
            print(f"{result}", end=" ")

#----------------------------------------------------------------------------------------------------------------------

prime_numbers = [2]
for i in range(3,200):
    is_prime = True
    for j in range(2, i):
        if i%j==0:
            is_prime = False

    if is_prime:
        prime_numbers.append(i)

for prime_number in prime_numbers:
    print(prime_number, end=", ")






























