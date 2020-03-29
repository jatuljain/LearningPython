"""
Map
Map applies a function to all the items in an input_list. Here is the blueprint:

Blueprint

map(function_to_apply, list_of_inputs)
Most of the times we want to pass all the list elements to a function one-by-one and then collect the output.
For instance:
"""

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

"""
Most of the times we use lambdas with map so I did the same. 
Instead of a list of inputs we can even have a list of functions!
"""


def multiply(x):
    return x*x


def add(x):
    return x+x


funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)


"""
4.2. Filter
As the name suggests, filter creates a list of elements for which a function returns true. Here is a short and concise example:

# Output: [-5, -4, -3, -2, -1]
The filter resembles a for loop but it is a builtin function and faster.
"""


number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
more_than_zero = list(filter(lambda x: x > 0, number_list))
print(more_than_zero)


"""
4.3. Reduce
Reduce is a really useful function for performing some computation on a list and returning the result. It applies a rolling computation to sequential pairs of values in a list. For example, if you wanted to compute the product of a list of integers.

So the normal way you might go about doing this task in python is using a basic for loop:

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
"""


from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product)