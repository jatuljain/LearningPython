import xml.dom.minidom
import xml.etree.ElementTree as ET

tree = ET.parse('E:\\Python\\ADI.XML')
root = tree.getroot()


print(root.tag)
p = tree.find("Asset_Name/p")     # Finds first occurrence of tag p in body

list(p.iter("Asset_Name"))
print(root[0][0][0].text)

element = root.find('Asset_Name')
print(element)

print(root.findall(".//*[@name='*']/Asset_Name"))