# A script to take the output of bowtie, parse it into the gene names as mapped and read names containing the real position
# 2011.12.20
# A. Black P.

# Usage: python checkMapAccuracy.py input.txt outputWithoutExtension

import sys

outfileName = sys.argv[2]
outfileCorrectNoErrors = open(outfileName + '.correctNoErrors', 'w')
outfileCorrectErrors = open(outfileName + '.correctErrors', 'w')
outfileIncorrectNoErrors = open(outfileName + '.incorrectNoErrors', 'w')
outfileIncorrectErrors = open(outfileName + '.incorrectErrors', 'w')

print 'Loading/counting data\n'

count1 = 0
count2 = 0
count3 = 0
count4 = 0

for newString in open(sys.argv[1]):
    data = newString.split('\t')
    if data[2] in data[0] and '_E' not in data[0]:
        outfileCorrectNoErrors.write(data[0] + '\t' + data[2] + '\n')
        count1 += 1
    elif data[2] in data[0] and '_E' in data[0]:
        outfileCorrectErrors.write(data[0] + '\t' + data[2] + '\n')
        count2 += 1
    elif data[2] not in data[0] and '_E' not in data[0]:
        outfileIncorrectNoErrors.write(data[0] + '\t' + data[2] + '\n')
        count3 += 1
    elif data[2] not in data[0] and '_E' in data[0]:
        outfileIncorrectErrors.write(data[0] + '\t' + data[2] + '\n')
        count4 += 1

print >> sys.stderr, count1, count2, count3, count4

print >> sys.stderr, 'Finished!'
