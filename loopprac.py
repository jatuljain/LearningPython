var_dict = {}

b = [1,2,3,4,5]
for x in b:
  var_dict["var_"+str(x)]=x

print(var_dict)

print(var_dict["var_5"])
