#!/usr/bin/env python3
import re
with open('Python_07.fasta', 'r') as fasta_file:
	for line in fasta_file:
		line = line.rstrip()
		fastas = re.match(r">(\S+)\s(.*)", line)
		if fastas:
			print("Extracted seq name:", fastas.group(1), "Extracted description:", fastas.group(2))
		else:
			pass
