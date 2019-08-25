# import xml.dom.minidom


from lxml import etree

import xml.etree.ElementTree as ET  
tree = ET.parse('E:\\Python\\ADI.XML')  
root = tree.getroot()

# find the first 'item' object
for elem in root:  
    print(elem.find('AMS').get('Asset_Name'))
	
# find all "item" objects and print their "name" attribute
for elem in root:  
    for subelem in elem.findall('AMS'):
	
		 # if we don't need to know the name of the attribute(s), get the dict
        print(subelem.attrib)      

        # if we know the name of the attribute, access it directly
        # print(subelem.get('ADI'))
# def parseXML(xmlFile):
    # """
    # Parse the xml
    # """
    # with open(xmlFile) as fobj:
        # xml = fobj.read()

    # root = etree.fromstring(xml)

    # for appt in root.getchildren():
        # for elem in appt.getchildren():
            # if not elem.text:
                # text = "None"
            # else:
                # text = elem.text
            # print(elem.tag + " => " + text)

# if __name__ == "__main__":
    # parseXML("E:\\Python\\ADI.XML")


# root = etree.parse(r"E:\\Python\\ADI.XML")
# Print the loaded XML
# print etree.tostring(root)
# from lxml import etree
# doc = etree.parse("E:\\Python\\ADI.XML")

# memoryElem = doc.find('ADI')
# print (memoryElem.text)        # element text
# print (memoryElem.get('Provider')) # attribute


# def main():
# use the parse() function to load and parse an XML file
   # doc = xml.dom.minidom.parse("E:\\Python\\ADI.XML");
  
# print out the document node and the name of the first child tag
   # print (doc.nodeName)
   # print (doc.firstChild.tagName)
  
# get a list of XML tags from the document and print each one
   # expertise = doc.getElementsByTagName(Metadata)
   # print ("%d expertise:" % expertise.length)
   # for skill in expertise:
     # print (skill.getAttribute("Content Value"))
 

# if name == "__main__":
# main(); 