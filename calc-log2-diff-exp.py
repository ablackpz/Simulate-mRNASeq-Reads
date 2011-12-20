# A script to take a combined file: three columns, key, geneExp1, geneExp2 and print out a log2(geneExp2/geneExp1) column.
# Original: 2011.11.29
# Original: A. Black P.
# Last: 2011.11.29
# Last: A. Black P.

# Usage: python calc-log2-diff-exp.py input.txt output.txt

import sys, makeRandomTestData, math

outfile = open(sys.argv[2], 'w')

print 'Loading/counting data\n'

count = 0

for newString in open(sys.argv[1]):
    newString = newString.rstrip()
    parts = newString.split('\t')
    if float(parts[2]) <= 0 or float(parts[1]) <= 0:
        ratio = 0
    else:
        ratio = math.log((float(parts[2]) / float(parts[1])), 2)
    outfile.write(parts[0] + '\t' + parts[1] + '\t' + parts[2] + '\t' + str(ratio) + '\n')
    count += 1


print count
print 'Finished!'
