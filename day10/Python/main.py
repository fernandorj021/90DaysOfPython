# Lists
list1 = [3,7,9,"Apple","Banana","Oranges",1,9,"Grapes"]

print(list1[2])
print(list1[-1])
print(list1[1:4])
print(list1[1:4])

list1[4]=99
print(list1)

list1.append("Cherry")
print(list1)

list1.insert(2,100)
print(list1)

list1.remove("Apple")
print(list1)

list1.clear()
print(list1)

del list1
print(list1)


# ---------------------------------------------------------------------------------------------------------------------
# Tuples (tuples are immutable. append, remove, insert and clear will not work)
tuple1 = (6,9,11,"Apple","Grapes",8,11)

print(tuple1[3])
print(tuple1[-1])

del tuple1
print(tuple1)

# ---------------------------------------------------------------------------------------------------------------------
# Dictionary
months = {
    "one": "January",
    "two": "February",
    "three": "March",
    "four": "April",
    "five": "May"
}

print(months)
print(months["three"])
print(months.get("three"))

print(len(months))

months["three"] = "December"
print(months)

del months["three"]
print(months)
print(len(months))

months.clear()
print(months)

del months
print(months)



