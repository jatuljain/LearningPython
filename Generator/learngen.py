def create_cube(n):
    for i in range(n):
        yield i**3

g = create_cube(5)
next(g)
print(list(create_cube(10)))
for x in create_cube(5):
    print(x)

