# path = "test.txt"
# file = open(path, "w+")

#-----------------------------------------------------------------------------------------------------------------------
# path = "test.csv"
# file = open(path, "w")
# file.write("This is a test csv file")

#-----------------------------------------------------------------------------------------------------------------------
# path = "test.txt"
# file = open(path, "r")

#-----------------------------------------------------------------------------------------------------------------------
# import os
# os.rename("test.txt", "test_file.txt")

#-----------------------------------------------------------------------------------------------------------------------
# path = "test.txt"
# file = open(path, "w")
# file.write("This is a text.txt file.")
# file.write(" For tests.")
# file.close()


#-----------------------------------------------------------------------------------------------------------------------
# path = "test.txt"
# file = open(path, "w")
# file.write("This is a text.txt file.")
# file.write(" For tests.")
# file.close()

#-----------------------------------------------------------------------------------------------------------------------
# path = "test.txt"
# file = open(path, "a")
# file.write(" Appended text.")
# file.close()

#-----------------------------------------------------------------------------------------------------------------------
# src = "test.txt"
# target = "test_copy.txt"
# file = open(src, "r")
# src_data = file.read()
# file.close()
#
# file = open(target, "a")
# file.write(src_data)
# file.close()

#-----------------------------------------------------------------------------------------------------------------------
# import os
#
# os.remove("test.csv")

#-----------------------------------------------------------------------------------------------------------------------
# import os
#
# os.rmdir("dir_test")

#-----------------------------------------------------------------------------------------------------------------------
# import shutil
#
# shutil.rmtree("dir_test")

#-----------------------------------------------------------------------------------------------------------------------
# path = "test.txt"
# with open(path,"w") as file:
#     file.write("test txt file!")

#-----------------------------------------------------------------------------------------------------------------------
# import csv
#
# dictionary = {
#     "Name": "Fernando",
#     "Job": "Tutorials",
#     "Company": "Udemy"
# }
#
# x = csv.writer(open("fernando.csv", "w"))
#
# for key, val in dictionary.items():
#     x.writerow([key, val])


#-----------------------------------------------------------------------------------------------------------------------
# import json
#
# dictionary = {
#     "Name": "Fernando",
#     "Job": "Tutorials",
#     "Company": "Udemy"
# }
#
# json = json.dumps(dictionary)
# x = open("fernando.json", "w")
# x.write(json)
# x.close()

#-----------------------------------------------------------------------------------------------------------------------
# dictionary = {
#     "Name": "Fernando",
#     "Job": "Tutorials",
#     "Company": "Udemy"
# }
#
# x = open("fernando.txt", "w")
# x.write(str(dictionary))
# x.close()

#-----------------------------------------------------------------------------------------------------------------------
import pickle

dictionary = {
    "Name": "Fernando",
    "Job": "Tutorials",
    "Company": "Udemy"
}

path = "fernando.pkl"

x = open(path, "wb")
pickle.dump(dictionary,x)
x.close()