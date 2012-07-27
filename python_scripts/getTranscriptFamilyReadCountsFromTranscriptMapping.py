# A script to get transcript family expression levels (reads per family) based on transcript mapping from bowtie (output from bowtie modified by awk to ease data handling) with one file listing where bowtie mapped the read and the other listing the actual transcript from which the read was derived
# Modified 2012.04.12
# Author A. Black P.

# Usage: python getTranscriptFamilyReadCountsFromTranscriptMapping.py geneGroups.input.txt bowtie.input.map.bowtie bowtie.input.map.actual output.bowtie.txt output.actual.txt

import makeRandomTestData, sys

infileGroups = sys.argv[1]
infileMap = sys.argv[2]
infileActual = sys.argv[3]
outfileMap = sys.argv[4]
outfileActual = sys.argv[5]

groups = {}
realExp = {}
print 'Reading groups data\n'
groups = makeRandomTestData.inputSimilarGroups(groups, infileGroups)
print 'Calculating mapping transcript family expression\n'
geneExp = makeRandomTestData.findGeneExpressionFromTranscripts2(groups, infileMap)
print 'Writing mapping transcript family expression\n'
tmp = makeRandomTestData.outputSimilarGroups(geneExp, outfileMap)
print 'Calculating actual transcript family expression\n'
actualExp = makeRandomTestData.findGeneExpressionFromTranscripts2(groups, infileActual)
print 'Writing actual transcript family expression\n'
tmp = makeRandomTestData.outputSimilarGroups(actualExp, outfileActual)
print 'Finished!'
