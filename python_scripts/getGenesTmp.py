# A script to take the output of bowtie, parse it into the gene names as mapped and read names containing the real position
# 2012.01.03
# A. Black P.

# Usage: python checkMapAccuracyPositives.py input.map input.geneExpLevels outputWithoutExtension

import sys, makeRandomTestData

outfileName = open(sys.argv[2], 'w')

print 'Loading/counting data\n'

count1 = 0
count2 = 0
count3 = 0
count4 = 0
fasta = makeRandomTestData.inputFastaSeq(sys.argv[1])

for key in fasta:
    name = key.lstrip()
    outfileName.write(name + '\t' + 'pass' + '\t' + '1' + '\n')


print >> sys.stderr, 'Finished!'
