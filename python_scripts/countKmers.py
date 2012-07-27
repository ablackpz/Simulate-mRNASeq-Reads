# A script to count the kmers in a seq to determine if there are duplicates within a gene
# Date Created: 2011.11.10
# Author: A. Black P.

# Usage: python countKmers.py inputfile.fa outputfile.fa

import makeRandomTestData, os, random, sys


k = 32
infileName = sys.argv[1]
outfile = open(sys.argv[2], 'w')
#genes = makeRandomTestData.inputFastaSeq(infileName)
#filename = 'DataSet130'
kmers = makeRandomTestData.countKmersFile(infileName, k)
count = 0
for key in sorted(kmers):
    outfile.write(key + '\t' +  str(kmers[key]) + '\n')
    count += 1

print >> sys.stderr, 'Number of kmers: ', count

print >> sys.stderr, 'Finished!'
