'''
Creating a variable number of variables based on the list values
'''

# Create a blank dictionary
var_dict = {}

#take a list
b = [1,2,3,4,5]
#Loop for a list
for x in b:
  var_dict["var_"+str(x)]=x

print(var_dict)
for keys, values in var_dict.items():
    print(keys, "=>" ,values)

print(var_dict["var_5"])
