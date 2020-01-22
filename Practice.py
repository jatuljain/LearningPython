# Python practise programs
from numpy import array
import re
from checkascii import countascii

'''
f=open("E:\Python\myfile.txt","r+")
# f.write("Hello! Learn Python on TutorialsTeacher.")
content = f.readlines()
print(content)

f.close()


## -----------------------------------------------------------------------------------------------
# Count of all the characters in a given string
# Simply iterate through the string and form a key in dictionary of newly occurred element or if element is already
# occurred, increase its value by 1.
str1 = "abcdabcdabcd"

all_freq = {}

for i in str1:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print ("Count of all characters in " + str1 + " is :\n "  +  str(all_freq))

## ------------------------------

# Python3 code to demonstrate  each occurrence frequency using
# collections.Counter()
from collections import Counter

# initializing string
test_str = "GeeksforGeeks"

# using collections.Counter() to get  count of each element in string
res = Counter(test_str)

# printing result
print ("Count of all characters in GeeksforGeeks is :\n " + str(res))

## ------------------------------

# Python3 code to demonstrate each occurrence frequency using
# dict.get()

# initializing string
test_str = "GeeksforGeeks"

# using dict.get() to get count
# of each element in string
res = {}

for keys in test_str:
	res[keys] = res.get(keys, 0) + 1

# printing result
print ("Count of all characters in GeeksforGeeks is : \n" + str(res))


## -----------------------------------------------------------------------------------------------
'''

# def getSuiteSrcDir():
#   builtin = BuiltIn.BuiltIn()
#   srcPath = builtin.get_variable_value('${SUITE SOURCE}')
#   if os.path.isfile(srcPath):
#     srcDir = os.path.dirname(srcPath)
#   elif os.path.isdir(srcPath):
#     srcDir = srcPath
#   else:
#     log.error("Suite source directory not found; src={0}".format(srcPath))
#     srcDir = ''
#   return srcDir
#
#
# getSuiteSrcDir("e:\python")
## -----------------------------------------------------------------------------------------------


## Print all even charcters
# def string_bits(str):
#   l1 = ""
#   for i in range(0,len(str), 2):
#     l1 = l1+(str[i])
#   return l1
#
# p = string_bits("Hello")
# print(p)

## -----------------------------------------------------------------------------------------------

# print(countascii("Hello"))
# host = {'speciality': 'speciality', 'Count': 'count' }
#
### The parameter weekday is True if it is a weekday, and the parameter vacation is
## True if we are on vacation. We sleep in if it is not a weekday or we're on vacation.
## Return True if we sleep in.
## sleep_in(False, False) → True  ## This means sleeping on weekend
## sleep_in(True, False) → False
## sleep_in(False, True) → True.  ## This means sleeping on Weekday but on vacation
# def sleep_in(weekday, vacation):
#     if(not weekday or vacation):
#         return True
#     else:
#         return False
# print(sleep_in(1,0))

# def sleep_in(weekday, vacation):
#     sleep = None
#     if (weekday == False) or (vacation == True):
#         sleep = True
#     elif (weekday == True) and (vacation == True):
#         sleep == True
#     elif (weekday == True) and (vacation == False):
#         sleep == False
#     return sleep

# print(sleep_in(1,1))

## -----------------------------------------------------------------------------------------------

# list = ["1", "4", "0", "6", "9"]
# list = [int(i) for i in list]
# list.sort()
# print (list)

## -----------------------------------------------------------------------------------------------


# xx = 'Asset_Class="movie" \
# Asset_ID="HYBR0000000000007565"\
# Asset_Name="POSTERSHOWGIRLS" \
# Creation_Date="2010-10-15" \
# Product="MOD" \
# Provider="Test_GL_MOD-1" \
# Provider_ID="Test_GL_MOD-1" \
# Verb="" \
# <Content Value="movie.ts"\
# </Asset>\
# <Asset>\
# <Metadata>\
# <AMS    Asset_Name="PREVIEWSHOWGIRLS"\
# Provider="Test_GL_MOD-1"\
# Product="MOD"\
# Version_Major="1"\
# Version_Minor="0"\
# Description="CMS80000MSMWFullMDTEST_CMS31 Preview"\
# Creation_Date="2010-12-07"\
# Provider_ID="Test_GL_MOD-1"\
# Asset_ID="HYBR0000000000007564"\
# Asset_Class="preview" Verb="" />\
# <App_Data App="MOD" Name="Type" Value="preview" />\
# Asset_Class="poster" \
# Asset_ID="HYBR0000000000007565"\
# Asset_Name="POSTERSHOWGIRLS" \
# Creation_Date="2010-10-15" \
# Product="MOD" \
# Provider="Test_GL_MOD-1" \
# Provider_ID="Test_GL_MOD-1" \
# Verb="" \
# <Content Value="new.jpg"/'


# postername = re.search(r".*Asset_Class=\"poster\".*Content Value=\"(.*)\"",xx)
# moviename = re.search(r".*Asset_Class=\"movie\".*Content Value=\"(.*)\".*</Asset>.*Asset_Class=\"preview\"",xx)
# print(r1)
# print(r2)
# print("poster name is : ", postername.group(1))
# print("movie name is : ", moviename.group(1))

# Paragraph = "<Asset>
# <Metadata>
# <AMS    Asset_Class="poster"
# Asset_ID="HYBR0000000000007565"
# Asset_Name="POSTERSHOWGIRLS"
# Creation_Date="2010-10-15"
# Description="CMS80000MSMWFullMDTEST_CMS31_Poster"
# Product="MOD"
# Provider="Test_GL_MOD-1"
# Provider_ID="Test_GL_MOD-1"
# Verb=""
# Version_Major="1"
# Version_Minor="0" />
# <App_Data App="MOD" Name="Type" Value="poster"/>
# <App_Data App="MOD" Name="Content_FileSize" Value="66650"/>
# <App_Data App="MOD" Name="Content_CheckSum" Value="f202d757106b0cd711824a00fd4ab397"/>
# </Metadata>
# <Content Value="new.jpg"/>
# </Asset>"


# print ("Paragraph is ", Paragraph)


# first = "this is my first Hello World"
# print (first)

# s1 = 'hello';
# s2 = "WORLD";
#
# print (s1+s2)
#
# s1=s1.upper()
# s2=s2.lower()
# print (s1+s2)
# print ("\n\n")

# split(delim = ‘’, ) – splits string according to the delimiter
# and returns list of substrings.
#
# splitedword = first.split()

# for temp in splitedword:
# print (temp)

## -----------------------------------------------------------------------------------------------

## Counting in list
# #===================
# list1 = [1,2,3 ,1, 6, 1 ,1]
#
# print (list1)
#
# print ("count of 1 in list", list1.count(1))

# del list1[2]  ## Deleting in a list by directly giving a value to be deleted
# print (list1)

# To check list membership or list contains
# res = 2 in list1

# print (res) # Result is True

# print ("\n\n maximum value in list " , max(list1))
# print ("\n\nMinimum value in list " , min(list1))

# list1.remove(1)
# print ("\n\nafter removing first 1 from list " , list1)

# list1.reverse()
# print ("\n\n after reverse list " , list1)


# list1.sort()
# print ("\n\n after sort list " , list1)


# =========================================
# Difference between array and list
# =========================================
# x = array([3, 6, 9, 12])
# x/3
# print("x after x/3\n", x)

'''
In the above example, your output would be:

array([1, 2, 3, 4])
lists are containers for elements having differing data types but arrays are used as containers for 
elements of the same data type.
'''

# y = [3, 6, 9, 12]
# y/3.0
# print(y)
# # >>> y/3.0
# # Traceback (most recent call last):
  # # File "<stdin>", line 1, in <module>
# # TypeError: unsupported operand type(s) for /: 'list' and 'float'





# print ("\n\n =============Tupple example started==========")
# tup = ('physics', 'chemistry', 1997, 2000);
# tup1 = (10, 20, 1997, 2000);
# print (tup);
# print ("\nmax tupple value :", max(tup1));
# print ("\n\n =============Tupple example Ended==========")


# print ("\n\n =============Dictionary example started==========")

# dict_1 = {'a':'5', 'b':'4', 'c':'5'}
# print ("\n dict value :", dict.keys(dict_1))


# print ("\n\n =============Dictionary example Finished==========")


# print ("\n\n =============Conditional example started==========")
# var = 300
# if var == 300:
# print ("The value of variable is ", var)
# else:
# print ("Not as expected")


# print ("\n\n =============Conditional example Finished==========")
