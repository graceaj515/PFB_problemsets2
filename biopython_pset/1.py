#!/usr/bin/env python3
import sys
from Bio import SeqIO
total_number_of_nucleotides = []
total_number_of_sequences = []
seq_GC_content = []
for seq_record in SeqIO.parse('Python_08.fasta', "fasta"):
	nucleotides_per_sequence = len(seq_record.seq)
	total_number_of_nucleotides.append(nucleotides_per_sequence)
	total_number_of_sequences.append('total_number_of_sequences')
	G_content = seq_record.seq.count('G')
	C_content = seq_record.seq.count('C')
	GC_content = (G_content + C_content) / len(seq_record.seq)
	seq_GC_content.append(GC_content)
print(f'The total number of sequences is {len(total_number_of_sequences)}.')
print(f' The total number of nucleotides is {sum(total_number_of_nucleotides)}.')
print(f' The average length of the sequences is {(sum(total_number_of_nucleotides))/(len(total_number_of_sequences))}.')
print(f' The shortest sequence length is {min(total_number_of_nucleotides)}.')
print(f' The longest sequence length is {max(total_number_of_nucleotides)}.')
print(f' The average GC content is {sum(seq_GC_content)/len(total_number_of_sequences)}.')
print(f' The highest GC content is {max(seq_GC_content)}.')
print(f' The lowest GC content is {min(seq_GC_content)}.')
