#Importando RegEx
import re
#Importando lectura de ficheros
import os
#Importando la barra de progreso
from progress.bar import ShadyBar
#import mysql.connector as mariadb

#Creo el csv con los datos y acceso escritura
destino = open("servel.csv", "w")

#Variable de la carpeta
servel = "servel/"

#Reviso si el directorio archivos existe, si no aviso al usuario
if os.path.isdir(servel) is True:

	#Cambio al directorio con los archivos
	os.chdir(servel)

#Leo el directorio y se guarda en array
directorio = os.listdir()

#Escribo la cabecera del csv
destino.write("NOMBRE;RUT;SEXO;DIRECCION;COMUNA\n")

#Agrego contador para saber la cantidad de archivos txt a procesar
#Estoy seguro que se puede hacer de una manera mas optimizada
contador = 0
for files in directorio:
	if files.endswith('.txt'):
		contador+=1


#Declarando la barra y el largo del contador anterior
bar = ShadyBar('Procesando archivos', max=contador, suffix='%(percent).1f%% - %(eta)ds')

chileno = {}

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

						#Separo los datos con el semicolon y asi poder trabajarlos como array
						datochileno = line.split(";")
						
						#Hay que averiguar porque existe unos saltos de linea en esos string convertidos en los casos 2, 3 y 4.

						if len(datochileno) == 2:
							destino.write(datochileno[0] + ";" + str(datochileno[1])[:-1] + ";NULO;NULO;NULO"+ "\n")
						
						#Por alguna razon el tercer valor tiene un salto de linea que corrompia el csv
						if len(datochileno) == 3:
							destino.write(datochileno[0] + ";" + datochileno[1] + ";" + str(datochileno[2])[:-1] + ";NULO;NULO\n")

						#Por alguna razon el cuarto valor tiene un salto de linea que corrompia el csv
						if len(datochileno) == 4:
							destino.write(datochileno[0] + ";" + datochileno[1] + ";" + datochileno[2] + ";" + str(datochileno[3])[:-1] + ";NULO\n")
						
						if len(datochileno) == 5:
							if datochileno[4][0].isdigit() is True:
								destino.write(datochileno[0] + ";" + datochileno[1] + ";" + datochileno[2] + ";" + datochileno[3] + ";NULO\n")
						
						if len(datochileno) > 5:
							if datochileno[5][0].isdigit() is True:
								destino.write(datochileno[0] + ";" + datochileno[1] + ";" + datochileno[2] + ";" + datochileno[3] + ";" + datochileno[4]+"\n")

		#Cierro el archivo para poder abrir el proximo
		origen.close()
#Tengo que revisar porque muestra este mensaje igual
else:
	print("la carpeta \"servel\"no existe")
