####### 
##Count the word in files
########
from collections import Counter
import re

# # Declare a variable and initialize it
# f = 101
# print(f)
# # Global vs. local variables in functions
# def somefunction():
# # global f
#     f = 'I am learning Python'
#     print(f)
# somefunction()
# print(f)

# file = open("E:\Python\debug.log")
#
# wordcount = Counter(file.read().split())
#
# for item in wordcount.items(): print("{}\t{}".format(*item))


file = open("E:\\Python\\file.txt")

content = file.read()
print ("\n\n",content, "\n\n")
matchObj = re.search(r'(.)-(.)', content, re.M|re.I)
if matchObj:
	print("matchObj.group() : ", matchObj.group())
	print("matchObj.group(1) : ", matchObj.group(1))
	print("matchObj.group(2) : ", matchObj.group(2))
else:
	print("No match!!")

### Print all the matches
matchObj = re.findall('(.)-(.)', content)
print("\nall the matches in file -\t", matchObj)
   
   
# for lines in file.readlines():
	# print "lines"


# speciality = ['Cardiology' , 'Nephrology', 'ENT', 'Oncology']
# print(speciality)
# count = [2, 7, 9, 1]
# print(count)
# host = {'speciality': speciality, 'Count': count }
# print(host)