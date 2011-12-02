# A script to take a file of simulated reads, read them all in, and randomly output them to a file.  The goal is to test whether read order matters in bowtie.
# Date Created: 2011.11.18
# Author: A. Black P.

# Usage: python randomizeReadOrder.py reads.fa randomReads.fa

import makeRandomTestData, os, random, sys

infileName = sys.argv[1]
outfileName = sys.argv[2]
genes = makeRandomTestData.inputFastaSeq(infileName)
numReads = len(genes)
for i in range(0, numReads):
    thisGeneName = random.choice(genes.keys())
    complete = makeRandomTestData.outputFastaSeq(outfileName, thisGeneName, genes[thisGeneName])
    genes.pop(thisGeneName)
