### Lambdas ###

sum_two_values = lambda first_value, second_value: first_value + second_value

print(sum_two_values(1,2))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2,2))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

my_sum = sum_three_values(5)(2,4)
print(my_sum)