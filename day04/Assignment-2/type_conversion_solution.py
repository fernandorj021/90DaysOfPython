integer_var = 5
float_var = float(integer_var)
string_var = str(integer_var)

print(f"The {type(float_var)} value of {integer_var} is {float_var}")
print(f"The {type(string_var)} value of {integer_var} is {string_var}")


float_var = 18.03
integer_var = int(float_var)
string_var = str(float_var)

print("\n")
print(f"The {type(integer_var)} value of {float_var} is {integer_var}")
print(f"The {type(string_var)} value of {float_var} is {string_var}")


string_var = "25"
integer_var = int(string_var)
float_var = float(string_var)

print("\n")
print(f"The {type(integer_var)} value of {string_var} is {integer_var}")
print(f"The {type(float_var)} value of {string_var} is {float_var}")