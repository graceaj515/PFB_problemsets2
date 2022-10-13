#!/usr/bin/env python3
import sys
dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
sequence_list = [((dna_list.index(dna)+1), dna, len(dna)) for dna in dna_list]
print(sequence_list)
