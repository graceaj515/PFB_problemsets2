#!/usr/bin/env python3
reading_the_file = open("Python_06.txt", "r")
writing_the_file = open("Python_06_uc.txt", "w")
for line in reading_the_file:
	line = line.rstrip()
	line = line.upper()
	writing_the_file.write(line+ "\n")
