#!/usr/bin/env python3
import sys
if int(sys.argv[1])>0:
	print('Positive')
	if int(sys.argv[1])<50:
#		print('It is smaller than 50.')
		data = int(sys.argv[1]) % 2
		if data == 0:
			print('It is smaller than 50 and even.')
		else:
			print('It is smaller than 50 and odd.')
	elif int(sys.argv[1])>50:
#		print('It is larger than 50.')
		division = int(sys.argv[1])% 3
		if division == 0:
			print('It is larger than 50 and divisible by 3.')
		else:
			print('It is larger than 50 and not divisble by 3.')
	else:
		print('The number is 50.')
elif int(sys.argv[1])<0:
	print('Negative')
else:
	print('0')
