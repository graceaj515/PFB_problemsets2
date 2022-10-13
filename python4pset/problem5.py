#!/usr/bin/env python3
import sys
n = 1000
new_product = 1
while n > 0: 
	product = n * (n-1)
	new_product = product * new_product
	n = n- 2
print(new_product)
