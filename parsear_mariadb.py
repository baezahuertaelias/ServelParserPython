#Importando RegEx
import re
#Importando lectura de ficheros
import os
#Importando la barra de progreso
from progress.bar import ShadyBar
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='root', database='servel')
cursor = mariadb_connection.cursor()

#Creo el csv con los datos y acceso escritura
#destino = open("servel.csv", "w")

#Variable de la carpeta
servel = "servel/"

#Reviso si el directorio archivos existe, si no aviso al usuario
if os.path.isdir(servel) is True:

	#Cambio al directorio con los archivos
	os.chdir(servel)

#Leo el directorio y se guarda en array
directorio = os.listdir()

#Escribo la cabecera del csv
#destino.write("NOMBRE;RUT;SEXO;DIRECCION;COMUNA;MESA\n")

#Agrego contador para saber la cantidad de archivos txt a procesar
#Estoy seguro que se puede hacer de una manera mas optimizada
contador = 0
for files in directorio:
	if files.endswith('.txt'):
		contador+=1

#Declarando la barra y el largo del contador anterior
bar = ShadyBar('Prcocesando archivos', max=contador, suffix='%(percent).1f%% - %(eta)ds')
#Recorriendo el array con los archivos

chileno ={}

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
					if not line.startswith(";"):
						hola = line.split(";")
							chileno['nombre'] = hola[0]
							chileno['rut'] = hola[1]
							chileno['sexo'] = hola[2]
							chileno['direccion'] = hola[3]
							if len(hola) == 4:
								chileno['comuna'] = " "
							else:
								chileno['comuna'] = hola[4]
						try:
							cursor.execute("INSERT INTO chilenos (nombre,rut,sexo,direccion,comuna) VALUES (%s,%s,%s,%s,%s)", (chileno['nombre'],chileno['rut'],chileno['sexo'],chileno['direccion'],chileno['comuna']))
							#print ("Insertando a: " + chileno['nombre'])
						except mariadb.Error as error:
							print("Error: {}".format(error))
						mariadb_connection.commit()
		origen.close()
	else:
		print("la carpeta \"servel\"no existe")