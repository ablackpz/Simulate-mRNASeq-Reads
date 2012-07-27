# A script to take the output of bowtie, parse it into the gene names as mapped and read names containing the real position
# 2012.01.03
# A. Black P.

# Usage: python checkMapAccuracyPositives.py input.map input.geneExpLevels outputWithoutExtension

import sys, makeRandomTestData

outfileName = sys.argv[3]
outfileTrueNegative = open(outfileName + '.trueNegative', 'w')
outfileFalseNegative = open(outfileName + '.falseNegative', 'w')

print 'Loading/counting data\n'

count1 = 0
count2 = 0
count3 = 0
count4 = 0
fasta = makeRandomTestData.inputFastaSeq(sys.argv[1])
simGenes = {}

for newString in open(sys.argv[2]):
    parts = newString.split('\t')
    simGenes[parts[0]] = parts[2]

for key in fasta:
#    data = newString.split('\t')
#    if len(key.split('_E')) > 3:
#        outfileTrueNegative.write(key + '\t' + fasta[key] + '\n')
#        count1 += 1
#or 'N' in fasta[key] or key not in simGenes.keys():
#
#    elif data[2] not in data[0] or len(data[2].split('_E')) > 3:
#    else:
    if len(key.split('_E')) < 4 and 'N' not in fasta[key] and key in simGenes.keys(): 
        outfileFalseNegative.write(data[0] + '\t' + data[2] + '\n')
        count2 += 1
    else:
        outfileTrueNegative.write(key + '\t' + fasta[key] + '\n')
        count1 += 1


print >> sys.stderr, count1, count2

print >> sys.stderr, 'Finished!'
