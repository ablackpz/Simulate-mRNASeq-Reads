# A script to count the kmers in a fasta file and output the kmers as a list of unique kmer genes
# Date Created: 2011.11.18
# Author: A. Black P.

# Usage: python writeUniqueKmers.py inputfile.fa outputfile.fa

import makeRandomTestData, os, random, sys



infileName = sys.argv[1]
#genes = makeRandomTestData.inputFastaSeq(infileName)
#filename = 'DataSet130'
kmers = makeRandomTestData.countKmersFile(infileName, 32)
count = 0
for key in kmers:
    complete = makeRandomTestData.outputFastaSeq(sys.argv[2], 'Kmer' + str(count), key)
    count += 1

print 'Number of kmers: ', count

print 'Finished!'
