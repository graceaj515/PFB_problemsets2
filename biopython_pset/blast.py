#!/usr/bin/env python3
from Bio import SeqIO
import re
seq_IDs = []
descriptions = {}
#for seq_record in SeqIO.parse("uniprot_sprot.fasta", "fasta"):
#	seq_IDs.append(seq_record.id)
#	for num in seq_IDs:
		#seq_description = re.search(r"OS=\w+ ", seq_record.id)
		#genus = seq_description.group(1)
		#species = seq_description.group(2)
		#print(seq_description)
#	print(len(seq_IDs)
with open('uniprot_sprot.fasta', 'r') as fasta:
	for line in fasta:
		line = line.rstrip()
		if line.startswith('>sp'):
			seq_description = re.search(r"OS=(\w+) (\w+)", line)
			if not seq_description:
				continue
			genus = seq_description.group(1)
			species = seq_description.group(2)
		else:
			continue
		if genus not in descriptions:
			descriptions[genus] = {}
		if species not in descriptions[genus]:
			descriptions[genus][species]= 0
		descriptions[genus][species] +=1
print(descriptions)
	
