#!/usr/bin/env python3
import sys
dna_seq = sys.argv[1]
dna_seq = dna_seq.replace('A','t')
dna_seq = dna_seq.replace('T','a')
dna_seq = dna_seq.replace('G','c')
dna_seq = dna_seq.replace('C','g')
dna_seq = dna_seq[::-1]
dna_seq = dna_seq.upper()
print(f"The reverse complement is 5' {dna_seq} 3'.")
