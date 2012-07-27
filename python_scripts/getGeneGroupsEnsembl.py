# A script to get gene groups from an ensembl file containing geneID \t transID
# Created 2012.02.10
# Author A. Black P.
# Modified 2012.04.09
# Author A. Black P.

# Usage: python getGeneGroupsEnsembl.py input.txt output.txt

import makeRandomTestData, sys

fileIn = sys.argv[1]
#fileNames = sys.argv[2]
fileOut = sys.argv[2]

groups = {}
#seqs = makeRandomTestData.inputFastaSeq(fileNames)
groups = makeRandomTestData.generateGroupsBowtie(groups, fileIn)
#groups = makeRandomTestData.restoreIdentifiers(groups,seqs)
groups = makeRandomTestData.reassignSimilarGroupKeys(groups)
tmp = makeRandomTestData.outputSimilarGroups(groups, fileOut)
#tmp = makeRandomTestData.inputSimilarGroups(groups, fileOut)
print 'Finished!'
