# A script to take the simulated reads for a gene and determine the actual coverage of the gene in a random + coverage simulation
# Date Created: 2011.11.15
# Author: A. Black P.

# Usage: python getSeqCoverageReal.py inputGene.fa inputReads.fa output.txt

import makeRandomTestData, os, random, sys, aabpPyLib


infileGeneName = sys.argv[1]
infileReadsName = sys.argv[2]
outfile = open(sys.argv[3], 'w')
genes = makeRandomTestData.inputFastaSeq(infileGeneName)
geneId = genes.keys()[0]
print geneId, len(genes[geneId])
geneLength = len(genes[geneId])
Coverage = [0] * geneLength
reads = makeRandomTestData.inputFastaSeq(infileReadsName)
for key in reads.keys():
    positionCut = key.split('Begin')
    parts = positionCut[1].split('End')
    print parts
    for i in range(int(parts[0]), int(parts[1])):
        Coverage[i] += 1

for i in range(0, geneLength):
    outfile.write(str(Coverage[i]) + '\n')

median = aabpPyLib.findMedian(Coverage)
print median

print 'Finished!'
