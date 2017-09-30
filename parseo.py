#Importando RegEx
import re
#Importando lectura de ficheros
import os

#Creo el csv con los datos y acceso escritura
destino = open("la dichosa bd.csv", "w")

#Leo el directorio y se guarda en array
directorio = os.listdir()

#Escribo la cabecera del csv
destino.write("NOMBRE;RUT;SEXO;DIRECCION;COMUNA;MESA\n")

#Recorriendo el array con los archivos
for files in directorio:
	#Filtro los archivos planos
	if files.endswith('.txt'):
		#Despues de filtrar, los abro con utf8 por las tildes y ecnes
		origen = open(files,'r',encoding='utf8')
		#Leyendo las filas y filtro las que estan malas
		for line in origen:
			if not "ELECTORAL" in line:
				if not "PROVINCIA" in line:
					#Uso RegEx para poder eliminar esos espacios grandes entre los textos
					line = re.sub('  +',';',line)
					#Cuando encuentra una fila mal formateada, no la agrego al csv 
					if line.startswith(";"):
						nada = ""
					else:
						#Agrego al csv
						destino.write(line)
origen.close()
destino.close()