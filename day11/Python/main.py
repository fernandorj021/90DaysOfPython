numbers = [1,2,3,4,5]

for num in numbers:
    if num == 3:
        print(f"The number {num} is at index {numbers.index(num)}")
        break

    print(num)

print("Outside of the loop")

#-----------------------------------------------------------------------------------------------------------------------
fruits = ["apples", "bananas", "cherry", "orange"]

search_for = "cherry"

for fruit in fruits:
    if fruit == search_for:
        print(f"{search_for} is found")
        break
    else:
        print(f"{search_for} not found")

#-----------------------------------------------------------------------------------------------------------------------
numbers = [1,2,3,4,5]

for num in numbers:
    if num == 3:
        continue

    print(num)

#-----------------------------------------------------------------------------------------------------------------------
word = "Python"

for char in word:
    if char == "t":
        continue
    print(char)

#-----------------------------------------------------------------------------------------------------------------------
# for loop in list and dictionaries
numbers2 = [1,2,3,4,5]

for num in numbers2:
    if num == 3:
        print(f"The number {num} is at index {numbers2.index(num)}")
        break


numbers_to_square = [1,2,3,4,5]
squares = []

for num in numbers_to_square:
    squares.append(num**2)

print(squares)


person  =  {"name": "John", "age": 30, "city": "New York"}
search_key = "age"

for k,v in person.items():
    print(k, v)

for k,v in person.items():
    if k == search_key:
        print(k,v)
        break

grades = {"Math": 90, "English": 85, "Science": 92}
scaled_grades = {}

for subject,score in grades.items():
    scaled_grades[subject] = score + 5

print(scaled_grades)

#-----------------------------------------------------------------------------------------------------------------------
# Nested for loop

for i in range(1,6):
    for j in range(1,10):
        print(f"i={i} : j={j}")








