#Importando RegEx
import re
#Importando lectura de ficheros
import os
#Importando la barra de progreso
from progress.bar import ShadyBar

#Cargo la barra de progreso
bar = ShadyBar('Cargantres')

#Creo el csv con los datos y acceso escritura
destino = open("la dichosa bd.csv", "w")

#Reviso si el directorio archivos existe, si no aviso al usuario
if os.path.isdir("servel/") is True:
	#Leo el directorio y se guarda en array
	directorio = os.listdir()

	#Escribo la cabecera del csv
	destino.write("NOMBRE;RUT;SEXO;DIRECCION;COMUNA;MESA\n")

	#Agrego contador para saber la cantidad de archivos txt a procesar
	#Estoy seguro que se puede hacer de una manera mas optimizada
	contador = 0
	for files in directorio:
		if files.endswith('.txt'):
			contador +=1

			#Declarando la barra y el largo del contador anterior
			bar = ShadyBar('Prcocesando archivos', max=contador)

			#Recorriendo el array con los archivos
			for files in directorio:
				#Filtro los archivos planos
				if files.endswith('.txt'):
					bar.next()
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
					bar.finish()
else:
	print("No existe la carpeta \"servel\"")