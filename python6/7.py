#!/usr/bin/env python3
annotated_sequences = {}
with open('Python_06.seq.txt','r') as sequencing_file:
	for line in sequencing_file:
		line = line.rstrip()
		seqName, DNA_sequence = line.split()
		DNA_sequence = DNA_sequence[::-1]
		DNA_sequence = DNA_sequence.replace('A','t')
		DNA_sequence = DNA_sequence.replace('T','a')
		DNA_sequence = DNA_sequence.replace('C','g')
		DNA_sequence = DNA_sequence.replace('G','c')
		DNA_sequence = DNA_sequence.upper()
		annotated_sequences[seqName]= DNA_sequence
for num_keys in annotated_sequences:
	print(num_keys, '\t', annotated_sequences[num_keys], '\n')
print('Generated the reverse compliment sequences.')
