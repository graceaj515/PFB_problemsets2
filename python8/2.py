#!/usr/bin/env python3]
with open('Python_08.fasta', 'r') as fasta_file:
	for line in fasta_file:
		line = line.rstrip()
		sequence = []
		if line.startswith('>'):
			pass
		else:
			sequence += line
	print(sequence)
