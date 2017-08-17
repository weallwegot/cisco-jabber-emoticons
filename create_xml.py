import os
import xml.etree.cElementTree as ET
from xml.dom import minidom

root = ET.Element("emoticons")

order_number = 1
for path, dirs, files in os.walk("resized_imgs"):
    for file_name in files:
        ext = file_name[-3:].lower()
        if ext == "png":
	        file_no_ext = file_name[:-4]
	        file_no_ext = file_no_ext.replace('(','').replace(')','').replace('&','').lower().decode('utf-8')
	        print file_no_ext
	        curr_emoticon_def = ET.SubElement(root,"emoticon",
	        	defaultKey=file_no_ext,
	        	image=file_name.decode('utf-8'),
	        	text=file_no_ext,
	        	order=str(order_number))
	        order_number += 1

# https://stackoverflow.com/questions/28813876/how-do-i-get-pythons-elementtree-to-pretty-print-to-an-xml-file
xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
with open("emoticonDefs.xml", "w") as f:
    f.write(xmlstr.encode('utf-8'))

