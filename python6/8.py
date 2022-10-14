#!/usr/bin/env python3
with open('Python_06.fastq.txt', 'r') as fastq:
	line_number = 0
	line_length = 0
	for line in fastq:
		line = line.rstrip()
		line_number = line_number + 1
		line_length = len(line) + line_length
	average_length = line_length / line_number
	print('The total number of lines is:', line_number, 'The total number of characters is:', line_length, 'The average line length is:', average_length)
