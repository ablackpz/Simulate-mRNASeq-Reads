# A script to create a groups file from the transcript family reads produced in getTranscriptFamilyReads.py that have been run through bowtie
# Created 2012.04.10
# Author A. Black P.

# Usage: python getTranscriptFamilyGroups.py input.txt output.txt

import makeRandomTestData, sys

fileIn = sys.argv[1]
fileOut = sys.argv[2]

groups = {}
groups = makeRandomTestData.generateGroupsBowtie(groups, fileIn)
#groups = makeRandomTestData.reassignSimilarGroupKeys(groups)
tmp = makeRandomTestData.outputSimilarGroups(groups, fileOut)
tmp = makeRandomTestData.outputSimilarGroupsOneToOne(groups, fileOut + 'OneToOne')
print 'Finished!'
