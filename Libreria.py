from xml.etree.ElementTree import parse,Element
xml = 'biblioteca.xml'
xmlParse= parse(xml)
raiz = xmlParse.getroot()
print(raiz)