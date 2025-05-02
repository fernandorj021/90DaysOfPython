print("Square Shaped Pattern")
input = int(input("Enter the size of square: "))


for i in range(input):
    for j in range(input):
        print("*", end=" ")
    print()

print("+++++++++++++++++")


for i in range(input):
    for j in range(i+1):
        print("*", end=" ")
    print()

print("+++++++++++++++++")

for i in range(input):
    for j in range(input-i):
        print("*", end=" ")
    print()

print("+++++++++++++++++")

# 4 = 0 1 2 3
for i in range(1, input+1):
    for j in range(input):
        if j == input-i:
            for k in range(i):
                print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("+++++++++++++++++")
# 4 = 0 1 2 3
# input = 6
count = 1
for i in range(input+1, 0, -1):
    for j in range(1, i):
        print(" ", end="")
        if j == i-1:
            for k in range(count):
                print("*", end=" ")
            count += 1
    print()

print("+++++++++++++++++")

# input = 6
input_2 = input
count = 1
for i in range(1, input + 1):
    for j in range(1, input_2 + 1):
        print("*", end=" ")
    input_2 -= 1
    print()
    for k in range(count):
        print(" ", end="")
    count += 1






