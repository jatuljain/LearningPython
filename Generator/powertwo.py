def PowTwoGen(max = 0):
    n = 0
    while n < max:
        print("2 to power ", n)
        yield 2 ** n
        n += 1

for pow in PowTwoGen(5):
     print( pow)