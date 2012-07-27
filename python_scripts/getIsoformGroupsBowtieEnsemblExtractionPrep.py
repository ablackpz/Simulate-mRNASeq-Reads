# A script to get isform groups from a fasta file
# Created 2012.02.10
# Author A. Black P.

# Usage: python getIsoformGroupsBowtie.py input.fa groupNum output.txt

import makeRandomTestData, sys

fileIn = sys.argv[1]
groupNum = sys.argv[2]
fileOut = sys.argv[3]
outfile = open(fileOut, 'w')

groups = {}
seqs = {}

groups = makeRandomTestData.generateGroupsBowtie(groups, fileIn)

for item in groups[groupNum]:
    outfile.write(item + '\n')


print 'Finished!'
