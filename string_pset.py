#!/usr/bin/env python3
import sys
dna_seq = sys.argv[1]
a_count = dna_seq.count('A') + dna_seq.count('a')
t_count = dna_seq.count('T') + dna_seq.count('t')
c_count = dna_seq.count('C') + dna_seq.count('c')
g_count = dna_seq.count('G') + dna_seq.count('g')
print(f"The number of A's is {a_count}, the number of T's is {t_count}, the number of C's is {c_count}, and the number of G's is {g_count}.")
AT_content = (a_count + t_count)/len(dna_seq)
GC_content = (g_count + c_count)/len(dna_seq)
print(f'The AT content is {AT_content} and the GC content is {GC_content}.')
