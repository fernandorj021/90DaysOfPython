favorite_colors = ["blue", "red", "green"]

print(f"List of favorite colors: {favorite_colors}")
print(f"Size of the list: {len(favorite_colors)} elements.")

#----------------------------------------------------------------------------------------------------------------------
favorite_colors = ["blue", "red", "green"]

color = input("Enter a favorite color: ")
favorite_colors.append(color)
print(f"Updated list of favorite colors: {favorite_colors}")

#----------------------------------------------------------------------------------------------------------------------
birthdate = (18,3,1982)
print(birthdate)

#----------------------------------------------------------------------------------------------------------------------
birthdate = (18,3,1982)
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

converted_birthdate = f"{birthdate[0]}-{months[birthdate[1]-1]}-{birthdate[2]}"
print(converted_birthdate)

#----------------------------------------------------------------------------------------------------------------------
book = {
    "title" : "90 Days of Python",
    "author" : "Levandovsky",
    "year" : 2020
}
print(book)

#----------------------------------------------------------------------------------------------------------------------
book = {
    "title" : "90 Days of Python",
    "author" : "Levandovsky",
    "year" : 2020
}
book["genre"] = "Programming"
print(book)

#----------------------------------------------------------------------------------------------------------------------
holidays_by_month = {
    "January": ["New Year's Day"],
    "February": ["Presidents' Day"],
    "March": [],
    "April": ["Easter"],
    "May": ["Labor Day (some countries)", "Memorial Day"],
    "June": ["Flag Day"],
    "July": ["Independence Day"],
    "August": [],
    "September": ["Labor Day (US)"],
    "October": ["Halloween"],
    "November": ["Thanksgiving"],
    "December": ["Christmas", "New Year's Eve"]
}

month = input("Enter the month: ")
holidays = holidays_by_month[month]

if len(holidays) > 0:
    for holiday in holidays:
        print(f"{holiday}")
else:
    print(f"Ooops no holidays in {month}...")

#----------------------------------------------------------------------------------------------------------------------







