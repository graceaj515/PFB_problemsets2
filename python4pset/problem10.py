#!/usr/bin/env python3
import sys
value1 = sys.argv[1]
value2 = sys.argv[2]
for num in range(int(sys.argv[1]), int(sys.argv[2])+1):
	if num % 2 != 0:
		print(num)
