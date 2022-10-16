#!/usr/bin/env python3
import re
with open('bionet.txt', 'r') as enzymes:
	count = 0
	for line in enzymes:
		line = line.rstrip()	
		count +=1
		if count >10:
			items = line.split()
			print(items)
		
