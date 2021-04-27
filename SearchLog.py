#############################################################################################################
### Open a directory and read all log files, print the log containging particular date and write to new file.
#############################################################################################################

import os
import glob
import re

logpath = os.listdir("D:\Python\Log")  
logpath = "D:\Python\Log"

print (logpath)
writelogfile = "D:\\Python\\Log\\newlog.log"
# for file in allfiles:
wfh = open (writelogfile, "a")

for filename in glob.glob(os.path.join(logpath, '*.log')):
        # file = os.path.splitext(os.path.basename(filename))[0]
        print ("filename : " + filename)
        rfh = open (filename , "r")
        lines = rfh.readlines()
        # print (line)
        for line in lines:
          searchObj = re.search( r'.*13/07/2018.*', line, re.M|re.I)
          if searchObj:
             print (searchObj.group())
             wfh.write(searchObj.group())
             wfh.write("\n")
             
        rfh.close()

wfh.close()