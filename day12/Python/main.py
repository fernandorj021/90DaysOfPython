i  = 1


while i<=10:
    square = i**2
    print(f"The square of {i} is {square}")
    i = i + 1

print("Outside of while loop")

# Nested while loop
outer_counter = 1

while outer_counter<=3:
    inner_counter = 1
    while inner_counter<=3:
        print(f"Outer: {outer_counter}, Inner: {inner_counter}")
        inner_counter += 1

    outer_counter += 1