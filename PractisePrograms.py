def myfunc(string):
	for i in range(len(string)):
		print(i)
		if i % 2 == 0:
			print("Inside even i")
			string[i]=string[i].lower()
		else:
			print("Inside odd i")
			string[i]=string[i].upper()
	return string

mystr = myfunc("Atul")
print(mystr)
### Print all the cities with lenght more than 5 characters
# finalcity = []
# visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# for city in visited_cities:
	# if len(city) >= 5 :
		# finalcity.append(city)
	
# print(finalcity)

### -- -------------------------------------------------------------------------------------------
# out = 0
# for num in range(1,1000):
	# print (num)
	# if (num % 3 == 0) or (num % 5 == 0):
		# print ("adding " ,int(num), int(out))
		# out = int(num) + int(out)
	
	# print (out)