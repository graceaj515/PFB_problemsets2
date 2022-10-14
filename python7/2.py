#!/usr/bin/env python3
import re
with open('Python_07_nobody.txt', 'r') as poem:
	new_poem = open('modifiedpoem.txt', 'w')
	new_poem.write(re.sub(r"Nobody", 'Irene', poem.read()))
	print('new file written')

		
