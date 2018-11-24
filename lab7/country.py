import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
root = ET.fromstring(country_data_as_string)
