import re
para ='''asdadadasd
    adasdad234234
    35
    454
    6@%#%^$%^
    #%#%
    36456$%^$%6
    35@#%$%4
    636#$^#SDFDAFHJHsv
    sSDFSDHD
    yegsv%$%^$UDFVSY$a%A&%^JSRFW$^U%Ha'''

fh = open('E:\\Automation\\WinFTP\\test.txt')   #### If wanna calculate the character from file
para = fh.read()

print(para)

counts = 0
countc = 0
countd = 0
print(para)

for i in para:
    if re.match(r'[a-z]', i):
        counts = counts+1
    if re.match(r'[A-Z]', i):
        countc = countc+1
    if re.match(r'[0-9]', i):
        countd = countd+1


print(countc , "Total capital character")
print(countd , "Total Digit")
print(counts, "Total Small Character")