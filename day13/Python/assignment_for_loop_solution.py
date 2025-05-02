sum = 0
for num in range(2, 11):
    if num%2 == 0:
        print(num, end=" ")
        sum += num
print()
print(f"The sum of the even numbers above is {sum}")


#----------------------------------------------------------------------------------------------------------------------

the_str = "Python Programming"
vowels = ["A","E","I","O","U","a","e","i","o","u"]

for letter in the_str:
    if letter in vowels:
        print(letter, end=" ")
