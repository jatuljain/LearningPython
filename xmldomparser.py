import xml.dom

doc = xml.dom.minidom.parse("E:\\Python\\ADI.XML")

# doc.getElementsByTagName returns NodeList
name = doc.getElementsByTagName("Metadata")[0]
print(name.firstChild.data)

Metadatas = doc.getElementsByTagName("Metadata")
for Metadata in Metadatas:
    print("Metadata", Metadata)
    Asset_Name = Metadata.getAttribute("Asset_Name")  # type: object
    Asset_ID = Metadata.getAttribute("Asset_ID")
    Asset_Class = Metadata.getAttribute("Asset_Class")
    print("Asset_Name:{}, Asset_ID:{}, Asset_Class:{}"
          .format(Asset_Name, Asset_ID, Asset_Class))
