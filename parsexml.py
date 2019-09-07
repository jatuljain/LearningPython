# parse an xml file by name
# from xml.dom import minidom
import xml.dom.minidom
import xml.etree.ElementTree as ET

# mydoc = minidom.parse('E:\\Python\\ADI.XML')
#
# AMS = mydoc.getElementsByTagName('Provider')
#
# print(AMS)
# # all items data
# print('\nAll item data:')
# for elem in AMS:
#     print(elem.firstChild.data)

doc = xml.dom.minidom.parse('E:\\Python\\ADI.XML')
print(doc.nodeName)
print(doc.firstChild.tagName)

Metadata = doc.getElementsByTagName("Asset")
print ("%d Metadata:" % Metadata.length)

for data in Metadata.findall("ASSET"):
    print(data.tag)