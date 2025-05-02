for i in range(1,11):
    if i%2!=0:
        continue

    print(i, end=", ")

#-----------------------------------------------------------------------------------------------------------------------
sum = 0
for i in range(1,51):
    if i % 3 == 0:
        continue

    sum += i
print(sum)

#-----------------------------------------------------------------------------------------------------------------------
prime_numbers = [2]
for i in range(3,13):
    is_prime = True
    for j in range(2, i):
        if i%j==0:
            is_prime = False
            continue

    if is_prime:
        prime_numbers.append(i)

for prime_number in prime_numbers:
    print(prime_number, end=", ")

#-----------------------------------------------------------------------------------------------------------------------
numbers = [1,2,3,4,5,6,7,8,9]
search_for = int(input("Search for number: "))

for number in numbers:
    if search_for == number:
        print(f"Number found at index: {numbers.index(number)}")
        break

#-----------------------------------------------------------------------------------------------------------------------
count = 1
for i in range(1,51):
    # print(i, end=", ")
    if i>20 and i % 2 == 0:
        if count <= 3:
            print(i, end=" ")
            count += 1
        else:
            break

#-----------------------------------------------------------------------------------------------------------------------
correct_password = "Python"
while True:
    password = input("Guess the password: ")
    if password == correct_password:
        print(f"Correct! The password is {correct_password}")
        break


#-----------------------------------------------------------------------------------------------------------------------




