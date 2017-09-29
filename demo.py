import re
origen = open("Alto Hospicio.txt",'r',encoding='utf8')
destino = open("Alto Hospicio.csv", "w")

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