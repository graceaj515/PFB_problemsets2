#!/usr/bin/env python3
import re
genes = {}
with open('Python_07.fasta','r') as fasta_file:
	for line in fasta_file:
		line = line.rstrip()
		fastas = re.match(r">(\S+)\s(.*)", line)
		if fastas:
			header = fastas.group(1).lstrip('gi|')
			genes[header] = ''
		else:
			genes[header] += line
	print(genes)
