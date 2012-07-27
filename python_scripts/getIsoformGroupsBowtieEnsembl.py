# A script to get isform groups from a fasta file
# Created 2012.02.10
# Author A. Black P.

# Usage: python getIsoformGroupsBowtie.py input.fa names.fa output.txt

import makeRandomTestData, sys

fileIn = sys.argv[1]
fileNames = sys.argv[2]
fileOut = sys.argv[3]

groups = {}
seqs = {}
for newString in open(fileNames):
    newString = newString.rstrip()
    ids = newString.split(',')
    seqs[ids[0]] = newString
groups = makeRandomTestData.generateGroupsBowtie(groups, fileIn)
groups = makeRandomTestData.restoreIdentifiersEnsembl(groups,seqs)
tmp = makeRandomTestData.outputSimilarGroups(groups, fileOut)

print 'Finished!'
