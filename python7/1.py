#!/usr/bin/env python3
import re
with open('Python_07_nobody.txt', 'r') as poem:
	for found in re.finditer(r"Nobody", poem.read()):
		print(found.group(), found.start(), found.end())
	
