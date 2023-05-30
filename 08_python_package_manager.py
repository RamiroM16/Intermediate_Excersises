### Pyhton Package Manager ###

# PIP

import numpy

print(numpy.version.version)
numpy_array = numpy.array([15, 24, 65, 23, 14, 40, 28])
print(type(numpy_array))

print(numpy_array * 2)

import pandas

# pip list
# pip uninstall pandas
# pip show numpy

# pip install requests
import requests

response = requests.get("https://www.instagram.com/")
print(response.status_code)
print(response.json)

# Arithmetics package

from my_package import arithmetics

print(arithmetics.sum_two_values(1, 4))

from myotherpackage import myotherarithmetics

print(myotherarithmetics.sum_two_values(1,4))