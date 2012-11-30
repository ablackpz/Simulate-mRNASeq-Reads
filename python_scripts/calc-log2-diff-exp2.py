# A script to take a combined file: three columns, key, geneExp1, geneExp2 and print out a log2(geneExp2/geneExp1) column.
# Original: 2011.11.29
# Original: A. Black P.
# Last: 2012.07.17
# Last: A. Black P.

# Usage: python calc-log2-diff-exp2.py input.txt output.txt

import sys, makeRandomTestData, math

outfile = open(sys.argv[2], 'w')

print 'Loading/counting data\n'

count = 0

for newString in open(sys.argv[1]):
    newString = newString.rstrip()
    parts = newString.split('\t')
    flag1 = 0
    flag2 = 0
    if parts[2] == 'NaN':
        parts[2] = 0
        flag2 = 1
    if parts[1] == 'NaN':
        parts[1] = 0
        flag1 = 1
    if float(parts[2]) <= 0 or float(parts[1]) <= 0:
        parts[2] = float(parts[2]) + 1
        parts[1] = float(parts[1]) + 1
#    else:
    ratio = math.log((float(parts[2]) / float(parts[1])), 2)
    if flag1:
        outfile.write(str(parts[0]) + '\t' + 'NaN' + '\t' + str(parts[2]) + '\t' + str(ratio) + '\n')
    elif flag2:
#        pass
        outfile.write(str(parts[0]) + '\t' + str(parts[1]) + '\t' + 'NaN' + '\t' + str(ratio) + '\n')
    else:
        outfile.write(str(parts[0]) + '\t' + str(parts[1]) + '\t' + str(parts[2]) + '\t' + str(ratio) + '\n')
    count += 1


print count
print 'Finished!'
