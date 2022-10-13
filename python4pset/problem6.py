#!/usr/bin/env python3
num_list = [101,2,15,22,95,33,2,27,72,15,52]
for num in num_list:
	if num % 2 == 0:
		print(num)
num_list = sorted(num_list)
even_numbers = 0
odd_numbers = 0
for num in num_list:
	print(num)
	if num % 2 == 0:
		even_numbers = even_numbers + num
	else:
		odd_numbers = odd_numbers + num
print(f'''Sum of even numbers: {even_numbers} 
Sum of odd numbers: {odd_numbers}.''')
