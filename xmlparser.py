from xml.dom import minidom

doc = minidom.parse("E:\\Python\\ADI.XML")

# doc.getElementsByTagName returns NodeList
name = doc.getElementsByTagName("App_Data")[0]
print(name.firstChild.data)
