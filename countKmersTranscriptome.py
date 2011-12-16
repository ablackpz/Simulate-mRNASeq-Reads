# A script to count the kmers in a transcriptome and output for each gene
# Date Created: 2011.12.08
# Author: A. Black P.

# Usage: python countKmersTranscriptome.py inputfile.fa outputfile.fa kLength

import makeRandomTestData, os, random, sys


k = int(sys.argv[3])
infileName = sys.argv[1]
outfileName = sys.argv[2]
kmers = makeRandomTestData.countKmersFile(infileName, k)
count = makeRandomTestData.outputDictionaryContent(outfileName, kmers)

print >> sys.stderr, 'Number of kmers: ', count

print >> sys.stderr, 'Finished!'
