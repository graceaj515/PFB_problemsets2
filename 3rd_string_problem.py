#!/usr/bin/env python3
import sys
dna_seq = sys.argv[1]
EcoRI_index = dna_seq.find('GAATTC')
EcoRI_end = EcoRI_index + 4
print(f'EcoRI startPos: {EcoRI_index +1}. EcoRI endPos: {EcoRI_end +2}.')
