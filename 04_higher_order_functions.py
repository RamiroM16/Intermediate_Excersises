### Higher Order Functions ###

from functools import reduce


def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_value(5,2,sum_one))
print(sum_two_values_and_value(5,2,sum_five))

### Closures ###

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(5))

print(sum_ten()(5))

### Built-in Higher Order Functions ###
numbers = [2, 5, 10, 21,3,30]

def multiply_two(number):
    return number * 2

# map
print(list(map(multiply_two, numbers)))     # map recibe una lista y a esa lista le aplica a cada iteracion dentro de la lista, la funcion dada
print(list(map(lambda number: number * 2, numbers)))

# filter

def filter_greater_that_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_that_ten, numbers)))
print(list(filter(lambda number: number>10, numbers)))

# Reduce
def sum_two_values(first_value, second_value):
    # print(first_value)
    # print(second_value)
    return first_value + second_value


print(reduce(sum_two_values, numbers))