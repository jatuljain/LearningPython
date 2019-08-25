# parse an xml file by name
from xml.dom import minidom

mydoc = minidom.parse('E:\\Python\\ADI.XML')

AMS = mydoc.getElementsByTagName('Provider')

print(AMS)
# all items data
print('\nAll item data:')  
for elem in AMS:  
    print(elem.firstChild.data)