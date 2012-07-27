# A script to take the output of bowtie, parse it into the gene names as mapped and read names containing the real position
# 2012.01.03
# A. Black P.

# Usage: python checkMapAccuracyPositives.py input.map input_al.map outputWithoutExtension

import sys, makeRandomTestData

outfileName = sys.argv[3]
outfileTruePositive = open(outfileName + '.truePositive', 'w')
outfileFalsePositive = open(outfileName + '.falsePositive', 'w')

print 'Loading/counting data\n'

count1 = 0
count2 = 0
#fasta = makeRandomTestData.inputFastaSeq(sys.argv[2])
for newString in open(sys.argv[1]):
    data = newString.split('\t')
    if data[2] in data[0] and len(data[2].split('_E')) < 4:
#and 'N' not in fasta[data[0]]:
        outfileTruePositive.write(data[0] + '\t' + data[2] + '\n')
        count1 += 1
#    elif data[2] not in data[0] or len(data[2].split('_E')) > 3:
    else:
        outfileFalsePositive.write(data[0] + '\t' + data[2] + '\n')
        count2 += 1

print >> sys.stderr, count1, count2

print >> sys.stderr, 'Finished!'
