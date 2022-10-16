#!/usr/bin/env python3
import re
with open('Python_07_ApoI.fasta', 'r') as Apo_file:
	cut_sites = re.finditer(r"([AG]AATT[CT])", Apo_file.read())
	for num in cut_sites:
		print(num.group(), num.start(), num.end())

