# A script to initialized a dictionary based on kmers from the transcriptome and count kmers in the reads
# Date Created: 2011.12.08
# Author: A. Black P.

# Usage: python countKmersReads.py reads.fa transcriptomeKmerCount.txt readKmerCount.txt kLength

import makeRandomTestData, os, random, sys


k = int(sys.argv[4])
infileReadsName = sys.argv[1]
infileTransName = sys.argv[2]
outfileName = sys.argv[3]
kmers = {}
kmers = makeRandomTestData.inputDictionaryContent(infileTransName, kmers)
kmers = makeRandomTestData.zeroInitializedDictionary(kmers)
kmers = makeRandomTestData.countKmersInitializedFile(infileReadsName, k, kmers)
#for key in sorted(kmers):
#    print key, kmers
count = makeRandomTestData.outputDictionaryContentNoKey(outfileName, kmers)

print >> sys.stderr, 'Number of kmers: ', count

print >> sys.stderr, 'Finished!'
