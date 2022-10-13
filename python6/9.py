#!/usr/bin/env python3
with open('Python_06.fasta.txt' , 'r') as fasta_file:
	fastaDict = {}
	for line in fasta_file:
		line = line.rstrip()	
		if 's' in line:
			header = line
			fastaDict[header] = ' '
		else:
			fastaDict[header] += line
	print(fastaDict)
			
		
