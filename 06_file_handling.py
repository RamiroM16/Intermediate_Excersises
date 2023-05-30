### File Handling ###
import os
# .txt file


txt_file = open("intermediate/my_file.txt","r+")
#txt_file.write("Mi nombre es Ramiro\nMi apellido es Mendoza\n25 años\nY mi lenguaje preferido es Python")
print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

#txt_file.write("\nAunque tambien me gusta Kotlin")
print(txt_file.readline())
txt_file.close()

#os.remove("intermediate/my_file.txt")

# .json file

import json
json_file = open("intermediate/my_file.json","w+")

json_text = {
             "Nombre": "Ramiro", 
             "Apellido": "Mendoza", 
             "Edad": 25,
             "languages": ["Python", "Kotlin", "JavaScript"], 
             1: "Python"}

json.dump(json_text,json_file, indent=2)
json_file.close()


with open("intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["Nombre"])

# .csv file
import csv
csv_file = open("intermediate/my_file.csv","w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "languages", "website"])
csv_writer.writerow(["Ramiro", "Mendoza", 25, "Python", "website"])
csv_writer.writerow(["Rubens", "", 25, "", ""])
csv_file.close()
with open("intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


# .xlsx file
#import xlrd # Debe instalarse el modulo

# .xml file
import xml
