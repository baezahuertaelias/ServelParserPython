#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
file = open("Alto del Carmen.txt",'r',encoding='utf8')

for line in file:
	print(re.sub('  +',';',line))
file.close()