#!/usr/bin/env python3
import re
with open('Python_07_ApoI.fasta', 'r') as Apo_fasta:
	seq = ''
	for line in Apo_fasta:
		line = line.rstrip().lstrip('>seq1')
		seq += line
		new_seq = re.sub(r"([AG])(AATT[CT])",r"\1^\2", seq)
	print(new_seq)
	fragments = new_seq.split("^")
	fragment_lengths = []
	for num in fragments:
		fragment_lengths.append(len(num))
	print(sorted(fragment_lengths))
