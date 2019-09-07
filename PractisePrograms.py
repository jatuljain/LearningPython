'''
Pass a string and print one capital letter and one small letter
'''
# def myfunc(pstr):
# 	nstr = ""
# 	for i in range(len(pstr)):
# 		if i % 2 == 0:
# 			# print("Inside even", i)
# 			nstr += pstr[i].lower()
# 		else:
# 			# print("Inside odd", i)
# 			nstr += pstr[i].upper()
# 	return nstr
#
# mystr = myfunc("Atul Jain")
# print(mystr)

'''
----------------------------------------------------------------------------------------------
'''



### Print all the cities with lenght more than 5 characters
# finalcity = []
# visited_cities = ["New York", "Shanghai", "Munich", "Toyko", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
# for city in visited_cities:
	# if len(city) >= 5 :
		# finalcity.append(city)
	
# print(finalcity)

### -- -------------------------------------------------------------------------------------------

'''
Print all the number between x,y which are divisible by 3 or 5
'''
out = 0
for num in range(1,100):
	# print (num)
	if (num % 3 == 0) or (num % 5 == 0):
		print ("adding " ,int(num), int(out))
		out = int(num) + int(out)
	
	print (out)