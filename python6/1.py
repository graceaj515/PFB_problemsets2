#!/usr/bin/env python3
import sys
mylist = [3, 14, 15, 9, 26, 5, 35, 9]
mylist2 = [60, 22, 14, 0, 9]
mySet = set(mylist)
mySet2 = set(mylist2)
intersection = mySet & mySet2 
difference = mySet - mySet2
union = mySet | mySet2
symmetrical_difference = mySet ^ mySet2 
print(intersection, difference, union, symmetrical_difference)
