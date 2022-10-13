#!/usr/bin/env python3
import sys
favorite_things = {'book': 'Twilight', 'song':'Circus by Britney Spears', 'tree' : 'pine'}
fav_thing = sys.argv[1]
fav_thing_key = sys.argv[2]
favorite_things[fav_thing] = sys.argv[2]

for keys in favorite_things:
	values = favorite_things[keys]
	print(keys, values, sep= "\t")
#print(favorite_things[sys.argv[1]])
#print(input(favorite_things.keys()))
#print(favorite_things.keys())
