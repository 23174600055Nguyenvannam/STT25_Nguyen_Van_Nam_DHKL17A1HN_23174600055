import xml.dom.minidom
def main():
   doc = xml.dom.minidom.parse("Nguyen_Van_Nam_DHKL17A1HN_23174600055\\example.xml")
   print(doc.nodeName)
   print(doc.firstChild.tagName)
   expertise = doc.getElementsByTagName("expertise")
   print("%d expertise:" % expertise.length)
   for skill in expertise:
       print(skill.getAttribute("name"))
if __name__=="__main__":
 main()