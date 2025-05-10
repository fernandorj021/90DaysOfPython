path="fernando.txt"

n = int(input("Enter the number of lines to read: "))

with open(path,"r") as file:
    for x in range(n):
        line = file.readline()

        if not line:
            break

        print(line)

#-----------------------------------------------------------------------------------------------------------------------
path="fernando.txt"

file = open(path,"a")
file.write("\nThis is an appended line.")
file.close()

file = open(path,"r")
content = file.readlines()
file.close()

for line in content:
    print(line)

#-----------------------------------------------------------------------------------------------------------------------
path="fernando.txt"

with open(path,"r") as file:
    content_list = file.readlines()

print(content_list)