#!/usr/bin/env python3
import sys
taxa = 'sapiens, erectus, neanderthalensis'
new_list = taxa.split(', ')
print(new_list)
print(new_list[1])
print(type(new_list))
print(sorted(new_list))
print(sorted(new_list, key= len))
