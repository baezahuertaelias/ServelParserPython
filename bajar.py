import wget
import xml.etree.ElementTree as ET
'''
nom_archivos = 'https://cdn.servel.cl/padronesdefinitivos/archivos.xml'
wget.download(nom_archivos);
'''
tree = ET.parse('archivos.xml')
root = tree.getroot()

for papa in root:
	for hijo in papa:
		for nieto in hijo:
			for chato in hijo:
				print(chato.name)