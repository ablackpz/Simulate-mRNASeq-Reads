# A script to count the number of times a gene name is present
# Orginal: 2011.10.17
# Orginal: A. Black P.
# Last Modified: 2011.10.26
# Last Author: A. Black P.

# Usage: python countGeneNames.py inputBowtieResults.map readLength input.geneLength outputGeneCount.out

import sys

print 'Loading/counting data\n'

count = 0
names = {}
readLength = sys.argv[2]

for newString in open(sys.argv[1]):
    newString = newString.rstrip()
    parts = newString.split('\t')
    parts[2] = parts[2].lstrip('>')
    if names.has_key(parts[2]):
        names[parts[2]] += 1
    else:
        names[parts[2]] = 1
    count += 1
print 'Gene List\n'

for newString in open(sys.argv[3]):
    newString = newString.rstrip()
    parts = newString.split('\t')
    parts[0] = parts[0].lstrip('>')
    parts1 = parts[0].split(' ')
    if names.has_key(parts1[0]):
        names[parts1[0]] = float(names[parts1[0]]) * float(readLength) / float(parts[1])

outfile = open(sys.argv[4], 'w')
for key in sorted(names.keys()):
    outfile.write(key + '\t' + str(names[key]) + '\n')
outfile.close()

print count
print 'Finished!'
