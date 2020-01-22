import os

# BasicHttpBinding_BundleServiceContract_TestSuite-GetBundleKeyValue_TestCase-GetBundleKeyValue-0-OK.txt
filename = "BasicHttpBinding_BundleServiceContract_TestSuite-GetBundleKeyValue_TestCase-GetBundleKeyValue-0-OK.txt"

print ("file name : " + filename)
file = os.path.splitext(os.path.basename(filename))[0]
print("file name with base 0 " + file)

rfindres = file.rfind('_TestSuite')
print('Position of _TestSuite :' + str(rfindres))
lenres = len('BasicHttpBinding_')
print('len of BasicHttpBinding_ :' + str(lenres))
findres = file.find('BasicHttpBinding_')
print("position of BasicHttpBinding_ :" + str(findres))
web_service = (file[len('BasicHttpBinding_'):file.rfind('_TestSuite')])
print("webserice name is between , length of BasicHttpBinding_ and position of _TestSuite and which is " + web_service)


method_name = (file[file.find('TestSuite-')+len('TestSuite-'):file.rfind('_TestCase')])
print(method_name)

# print(file[17:38])