#!/usr/bin/env python3
import re
genes = {}
reads = set()
with open('bowtie2.sam', 'r') as rna_file:
	for line in rna_file:
		line = line.rstrip()
		line = line.split('\t')
		read = line[0]
		gene = line[2]
		gene = re.match(r"(\S+)\^", gene)
		gene = gene.group(1)
		if gene not in genes:
			genes[gene] = [read]
		if gene in genes:
			if read not in genes[gene]:
				genes[gene].append(read)
			else:
				continue
for key, value in genes.items():
	print(key, len(value))

		
	
