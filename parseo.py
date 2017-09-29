import re
import os

destino = open("la dichosa bd.csv", "w")
directorio = os.listdir()

destino.write("NOMBRE;RUT;SEXO;DIRECCION;COMUNA;MESA\n")

for files in directorio:
	if files.endswith('.txt'):
		origen = open(files,'r',encoding='utf8')
		for line in origen:
			if not "ELECTORAL" in line:
				if not "PROVINCIA" in line:
					line = re.sub('  +',';',line)
					if line.startswith(";"):
						nada = ""
					else:
						destino.write(line)
origen.close()
destino.close()