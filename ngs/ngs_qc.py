#!/usr/bin/env python3
with open('SRR21901339.fastq', 'r') as fasta_file, open('Ecoli_trimmed_reads.fastq', 'w') as trimmed_file:
	list_of_indexes = []
	line_count = 1
	for line in fasta_file:
		min_Phred = 30	
		if line_count % 4 == 0:
			line_index = len(line)
			for num in line[::-1]:
				Phred = ord(num) - 33
				if Phred >= min_Phred:
					line = line[0:(line_index -1)]
					list_of_indexes.append(line_index-1)
					break
				line_index -=1
		line_count = line_count +1

################## YOU HAVE YOUR LIST OF LENGTHS OF CLEAN FILES, NOW YOU NEED TO 
with open('SRR21901339.fastq', 'r') as fasta_file, open('Ecoli_trimmed_reads.fastq', 'w')     as trimmed_file:
	n = 1
	second_line_count = 1
	for line in fasta_file:
		if second_line_count == 1:
			trimmed_file.write(line)
		if line_count == 2:
			trimmed_file.write(line)
		if line_count == 3:
			line = line[:list_of_indexes[0]]
			trimmed_file.write(line)
		if line_count == 4:
			line = line[:list_of_indexes[0]]
			trimmed_file.write(line)
		if  line_count == (3*n +4): 
			line = line[:list_of_indexes[n]]
		n+=1

