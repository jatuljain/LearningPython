'''
Python Generator Expression
Simple generators can be easily created on the fly using generator expressions. It makes building generators easy.

Same as lambda function creates an anonymous function, generator expression creates an anonymous generator function.

The syntax for generator expression is similar to that of a list comprehension in Python. But the square brackets
are replaced with round parentheses.

The major difference between a list comprehension and a generator expression is that while list comprehension
produces the entire list, generator expression produces one item at a time.

They are kind of lazy, producing items only when asked for. For this reason, a generator expression is much
 more memory efficient than an equivalent list comprehension.
*/
'''


# Intialize the list
my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)
# Output: 1
print(next(a))

# Output: 9
print(next(a))

# Output: 36
print(next(a))

# Output: 100
print(next(a))

# Output: StopIteration
next(a)