### Regular Expressions ###

import re

my_string = "Esta es la leccion numero 7: Leccion llamada Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de ficheros"

match = re.match("Esta es la leccion", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la leccion", my_other_string)
# if not(match == None):
# if match != None:
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start : end])

#print(re.match("Expresiones regulares", my_string))

# Search

search = re.search("Esta es la leccion", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("leccion", my_string, re.I)
print(findall)

# split

print(re.split(":", my_string))

# sub
print(re.sub("Expresiones Regulares", "RegEx", my_string, re.I))
print(re.sub("leccion|Leccion", "LECCION", my_string, re.I))
print(re.sub("[l|L]eccion", "LECCION", my_string, re.I))

# Patterns

pattern = r"[l|L]eccion"
print(re.findall(pattern, my_string))

pattern = r"[l|L]eccion|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-5]"
print(re.findall(pattern, my_string))

# email validation regular expression (regex)

email = "rmd161297@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))