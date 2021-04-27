#!/usr/bin/env python3
import fileinput
import re

# with fileinput.FileInput("E:\\Python\\ADI.XML", inplace=True, backup='.bak') as file:
with open('E:\\Python\\ADI.XML', 'r') as file:
	# content = file.read()
	content=file.read().replace('\n', '')

postername = re.search(r".*Asset_Class=\"poster\".*Content Value=\"(.*)\"",content)
print("poster name is : ", postername.group(1))
previewame = re.search(r".*Asset_Class=\"preview\".*Content Value=\"(.*)\".*</Asset>.*Asset_Class=\"poster\"",content)
print("preview name is : ", previewame.group(1))
	

# print(content.replace(r"postername.group(1)", "new1.jpg"), end='')

# postername.group(1)
    # for line in content:
		# postername = re.replace(r".*Asset_Class=\"poster\".*Content Value=\"(.*)\"",line)

        # print(line.replace(r"postername.group(1)", "new1.jpg"), end='')
		# print("poster name is : ", line)

 
# for line in fileinput.input():
    # line = re.sub(r'\* \[(.*)\]\(#(.*)\)', r'<h2 id="\2">\1</h2>', line.rstrip())
    # print(line)
 
 
 
 
 # <Asset>
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
# </Asset>