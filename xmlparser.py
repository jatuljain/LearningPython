from xml.dom import minidom
from xml.dom.minidom import parse, parseString

doc = parse("E:\\Python\\ADI.XML")
datasource = open('E:\\Python\\ADI.XML')
dom2 = parse(datasource)  # parse an open file

dom3 = parseString('<Asset>.*</Asset>')

# doc.getElementsByTagName returns NodeList
# name = doc.getElementsByTagName("App_Data")[0]
# print(name)
# just to check git pull from this location
