import re


fh = open('E:\\Python\\Log\\logfile4.log')
fhw = open('E:\\Python\\Log\\newlogfile4.log', "w+")

line = fh.readline()
ipregex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
my_regex = r"" +ipregex

while line :
    # print(line)
    line = fh.readline()
'''##### To match multiple conditions'''
    if re.match(my_regex + "( is reachable| is not reachable)", line):
        fhw.write(line)

# content = file.read()
# print (content)

newfilec = fhw.read()
print (newfilec)
fh.close()
fhw.close()