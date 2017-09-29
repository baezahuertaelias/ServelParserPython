import re
file = open("Alto Hospicio.txt",'r',encoding='utf8')

for line in file:
	if not "ELECTORAL" in line:
		if not "PROVINCIA" in line:
			line = re.sub('  +',';',line)
			if line.startswith(";"):
				nada = ""
			else:
				print(line)
file.close()