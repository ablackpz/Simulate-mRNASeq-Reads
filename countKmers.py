# A script to count the kmers in a seq to determine if there are duplicates within a gene
# Date Created: 2011.11.10
# Author: A. Black P.

# Usage: python countKmers.py inputfile.fa

import makeRandomTestData, os, random, sys


k = 32
infileName = sys.argv[1]
#genes = makeRandomTestData.inputFastaSeq(infileName)
#filename = 'DataSet130'
kmers = makeRandomTestData.countKmersFile(infileName, k)
count = 0
for key in kmers:
    print key, kmers[key]
    count += 1

print 'Number of kmers: ', count

print 'Finished!'
