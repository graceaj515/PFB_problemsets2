#!/usr/bin/env python3
seq_com = {}
with open('Python_08.fasta', 'r') as fasta:
	for line in fasta:
		line = line.rstrip()
		if ">" in line:
			header = line.lstrip('>').split(' ')
			seq_id = header[0]
			seq_com[seq_id] = {'A':0, 'T':0, 'G':0, 'C':0}
		else:
			for nucleotide in line:
				seq_com[seq_id][nucleotide] += 1
				print(seq_com)
			
