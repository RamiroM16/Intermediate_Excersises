### Error types ###

# SyntaError

#print "Hola gente"
print("Hola gente")

# NameError

#print(name)
name=0
print(name)

# IndexError

my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5])

# ModuleNotFoundError
#import maths
import math

# AttributeError
#print(math.PI)
print(math.pi)

# KeyError
my_dict = {"Nombre": "Ramiro", "Apellido": "Mendoza", "Edad": 25, 1: "Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"])

# TypeError
#print(my_list["0"])
print(my_list[0])

# ImportError
#from math import Pi 
from math import pi

# ValueError
my_int = int("10")
#my_int = int("10 años")
print(type(my_int))

# ZeroDivisionError
#print(4/0)
print(4/2)