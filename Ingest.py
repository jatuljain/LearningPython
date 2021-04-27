#!/usr/bin/env python3
import fileinput
import re


print("This is just to submit for review")
with open('E:\\Python\\ADI.XML', 'r') as file:
	# content = file.read()
	content=file.read().replace('\n', '&')

# print("file content is: ", content)	


#Extracting Package Asset_Name
packageAssetName = re.search(r"AMS.*Asset_Name=\"(.*)\".*Provider=\"Test_GL_MOD-1\".*Asset_Class=\"package\"",content)
## print("package name is : ", packageAssetName)
packageAssetName =  packageAssetName.group(1)
print("Package Asset_Name is : ", packageAssetName)

###Extracting Package Asset_ID name
# packageAssetID = re.search(r".*Provider_ID=\"Test_GL_MOD-1\".*Asset_ID=\"(.*)\".*Asset_Class=\"package\"",content)
### print("package asset id is : ", packageAssetID)
# Package_Asset_ID =  packageAssetID.group(1)
# print("poster Asset_ID is : ", Package_Asset_ID)


########################################
####Package finished##########
########################################

##Extracting Title Asset_Name
titleAssetName = re.search(r".*Asset_Class=\"package\".*Asset_Name=\"(.*)\".*Provider=\"Test_GL_MOD-1\".*Asset_Class=\"title\"",content)
# print("Title asset full name is : ", titleAssetName)
titleAssetName =  titleAssetName.group(1)
print("Title Asset_Name is : ", titleAssetName)

#Extracting Title Asset_ID
titleAssetID = re.search(r".*Provider_ID=\"Test_GL_MOD-1\".*Asset_ID=\"(.*)\"&.*Asset_Class=\"title\"",content)
# print("Title Asset ID is : ", titleAssetID)
titleAssetID =  titleAssetID.group(1)
print("Title Asset_ID is : ", titleAssetID)

#Extracting Title Asset_Value
titleAssetValue = re.search(r".*Asset_Class=\"title\".*Name=\"Title\" Value=\"(.*)\" />.*Name=\"Summary_Short\"",content)
# print("Title Asset ID is : ", titleAssetValue)
titleAssetValue =  titleAssetValue.group(1)
print("Title Asset_Value is : ", titleAssetValue)

########################################
####Title finished##########
########################################

#Extracting Movie Asset_Name


##Extracting Title Asset_Name
MovieAssetName = re.search(r".*Asset_Class=\"title\".*Asset_Name=\"(.*)\".*Provider=\"Test_GL_MOD-1\".*Asset_Class=\"movie\"",content)
# print("Movie asset full name is : ", MovieAssetName)
MovieAssetName =  MovieAssetName.group(1)
print("Movie Asset_Name is : ", MovieAssetName)

#Extracting Movie Asset_ID
movieAssetID = re.search(r".*Provider_ID=\"Test_GL_MOD-1\".*Asset_ID=\"(.*)\"&.*Asset_Class=\"movie\"",content)
# print("Title Asset ID is : ", movieAssetID)
movieAssetID =  movieAssetID.group(1)
print("Movie Asset_ID is : ", movieAssetID)


##Extracting Movie
moviefilename = re.search(r".*Asset_Class=\"movie\".*Content Value=\"(.*)\".*</Asset>.*Asset_Class=\"preview\"",content)
print("Movie file name is : ", moviefilename.group(1))

########################################
####Movie finished##########
########################################

##Extracting Poster
# postername = re.search(r".*Asset_Class=\"poster\".*Content Value=\"(.*)\"",content)
##### print("poster name is : ", postername)
# print("poster name is : ", postername.group(1))

###Extracting Preview
# previewname = re.search(r".*Asset_Class=\"preview\".*Content Value=\"(.*)\".*</Asset>.*Asset_Class=\"poster\"",content)
# print("preview name is : ", previewname.group(1))


###Extracting Movie
# moviename = re.search(r".*Asset_Class=\"movie\".*Content Value=\"(.*)\".*</Asset>.*Asset_Class=\"preview\"",content)
# print("Movie name is : ", moviename.group(1))





# content = content.replace(postername.group(1), "new2.jpg")
# content = content.replace(previewname.group(1), "newpreview2.jpg")
# content = content.replace(moviewname.group(1), "newmovie2.jpg")



# print("new content is : ", content)
content=content.replace('&', '\n')
# print("final content is : \n", content)
file.close

#### Final open a file and write with updated data.
# file= open("E:\\Python\\ADI.XML","w")
# file.write(content)
# file.close
