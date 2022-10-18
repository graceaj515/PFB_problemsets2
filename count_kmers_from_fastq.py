#!/usr/bin/env python

import os, sys
import re
from sequence_to_kmer_list import sequence_to_kmer_list
from fastq_file_to_sequence_list import seq_list_from_fastq_file
from operator import itemgetter, attrgetter

## method: count_kmers(kmer_list)
##
##  Counts the frequency of each kmer in the given list of kmers
##
##  input parameters:
##
##  kmer_list : list of kmers (type: list)
##               ie.  ["GATC", "TCGA", "GATC", ...]
##
##
##  returns kmer_counts_dict : dict containing ( kmer : count )
##                    ie.  {  "GATC" : 2,
##                            "TCGA" : 1,
##                             ...       }


def count_kmers(kmer_list):
	
	kmer_count_dict = dict()
	for num in kmer_list:
		if num not in kmer_count_dict:
			kmer_count_dict[num] = 0
		if num in kmer_count_dict:
			kmer_count_dict[num] += 1
	return kmer_count_dict


def main():

    progname = sys.argv[0]

    usage = "\n\n\tusage: {} filename.fastq kmer_length num_top_kmers_show\n\n\n".format(
        progname
    )

    if len(sys.argv) < 4:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    kmer_length = int(sys.argv[2])
    num_top_kmers_show = int(sys.argv[3])

    seq_list = seq_list_from_fastq_file(fastq_filename)

    all_kmers = []
    #######################
    ## Step 1:
    ## begin your code, populate 'all_kmers' list with the
    ## collection of kmers from all sequences
    n = 0
    for num in seq_list:
        kmers = sequence_to_kmer_list(seq_list[n], kmer_length)
        all_kmers.append(kmers)
        n = n+1
    all_kmers_real = []
    for num in all_kmers:
        for item in num:
            all_kmers_real.append(item)
    print(all_kmers_real)






    ## end your code
    #######################
    kmer_count_dict = count_kmers(all_kmers_real)  # see step 2 above. You implement this. :-)
    unique_kmers = list(kmer_count_dict.keys())
    unique_kmers_sorted = sorted(kmer_count_dict.items(), key=itemgetter(1), reverse = True)
    print(unique_kmers_sorted)

    #########################
    ## Step 3: sort unique_kmers by abundance descendingly
    ## (Note, you can run and test without first implementing Step 3)
    ## begin your code       hint: see the built-in 'sorted' method documentation
   # for num in unique_kmers:
       # print(all_kmers.count(num))


    ## end your code

    ## printing the num top kmers to show
   # top_kmers_show = sorted(unique_kmers[0:num_top_kmers_show])
    #for kmer in top_kmers_show:
     #   print("{}: {}".format(kmer, kmer_count_dict[kmer]))

    sys.exit(0)  # always good practice to indicate worked ok!


if __name__ == "__main__":
    main()
