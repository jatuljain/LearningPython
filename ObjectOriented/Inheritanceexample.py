class Parentclass():
    v1 = "from parent class - v1"
    v2 = "from parent class - v2"

class childclass(Parentclass):
     v1 = "from child class -v1"

co = childclass()
print(co.v1)  # if defined in child output-- "from child class -v1"
print(co.v2)  ## if not defined in child class output -- from parent class - v2