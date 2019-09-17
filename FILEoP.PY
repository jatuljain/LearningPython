import re
import os
import sys
import readjson as rj


filenamenew = "E:\\Python\\git_projects\\svt-mmp - Copy.json"

rj.readjson(filenamenew)

# print(pathvar)
# with open("E:\\Python\\debug.log") as d:
#
# 	for i in d:
# 		print(i)
#


'''
file = open("E:\\Python\\file.txt")

# content = file.read()
# print (content)

# linewise = file.readline(100)
# print (linewise)
for line in file:
	# print (line)
	matchObj = re.search("(.*)-(.*)", line, re.M|re.I)
	if matchObj:
		print ("matchObj.group() : ", matchObj.group())
		print ("matchObj.group(1) : ", matchObj.group(1))
		print ("matchObj.group(2) : ", matchObj.group(2))
	# else:
		# print ("No match!!")
file.close()


# So with this triple quptes this will become commented
# This is the output of above programe
# E:\Python\git projects>py FILEoP.PY
# matchObj.group() :  876-976784
# matchObj.group(1) :  876
# matchObj.group(2) :  976784
# matchObj.group() :  14367-2345
# matchObj.group(1) :  14367
# matchObj.group(2) :  2345
# matchObj.group() :  09872-0934
# matchObj.group(1) :  09872
# matchObj.group(2) :  0934
# matchObj.group() :  234-769843
# matchObj.group(1) :  234
# matchObj.group(2) :  769843
# matchObj.group() :  9876-76234
# matchObj.group(1) :  9876
# matchObj.group(2) :  76234


# with open("E:\\Python\\file.txt") as f:
# 	for line in f:
# 		# print("this is my lines " + line)
# 		matchObj = re.search(r'(.*)-(.*)', line, re.M|re.I)
# 		if matchObj:
# 			print ("matchObj.group() : ", matchObj.group() + " " + line)
# 			print ("matchObj.group(1) : ", matchObj.group(1) + " " + line)
# 			print ("matchObj.group(2) : ", matchObj.group(2)  + " " + line)
# 		else:
# 			print ("No match!! in " + line)
#
'''