city = str(input("Enter the city name "))
doctype = str(input("Enter the doctor type none if unknown "))

#If doc type is not given
def type_not_given():
    type = location.iter()
    for info in type:
        print(info.tag , info.text)

#If doc tag is given
def type_given():
    doc_type = location.findall(doctype)
    for doc in doc_type:
        if doc != None:
            type = doc.iter()
            for info in type:
                print(info.tag , info.text)
        else:
            print("Not found")

import xml.etree.ElementTree as ET
tree = ET.parse('items2.xml')
root = tree.getroot()
location = root.find(city)


if doctype == "none":
    type_not_given()
else:
    type_given()







         
        
      
      
