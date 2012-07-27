# A script to get isform groups from a fasta file
# Created 2012.02.06
# Author A. Black P.

# Usage: python getIsoformGroups.py input.fa output.txt scorePercentage

import makeRandomTestData, sys

fileIn = sys.argv[1]
fileOut = sys.argv[2]
score = float(sys.argv[3])

print makeRandomTestData.getSimilarGroups(fileIn, fileOut, score)

print 'Finished!'
