#!/usr/bin/env python3 
with open('alpaca_all_genes.txt', 'r') as all_genes:
	gene_set = set()
	for line in all_genes:
		if 'Gene' in line:
			pass
		else:
			line= line.rstrip()
			gene_set.add(line)
with open('alpaca_stemcellproliferation_genes.txt', 'r') as stemcell_genes:
	stem_cells = set()
	for line in stemcell_genes:
		if 'Gene' in line:
			pass
		else:
			line= line.rstrip()
			stem_cells.add(line)
with open('alpaca_pigmentation_genes.txt', 'r') as pigmentation_genes:
	pigmentation = set()
	for line in pigmentation_genes:
		if 'Gene' in line:
			pass
		else:
			line = line.rstrip()
			pigmentation.add(line)
not_proliferation = gene_set - stem_cells
both_proliferation_and_pigment = stem_cells & pigmentation
#print(both_proliferation_and_pigment)
#print(pigmentation)
with open('alpaca_transcriptionfactors.txt', 'r') as transcriptionfactors:
	TFs = set()
	for line in transcriptionfactors:
		if 'Gene' in line:
			pass
		else:
			line = line.rstrip()
			TFs.add(line)
TFs_for_proliferation = stem_cells & TFs
print(TFs_for_proliferation)
