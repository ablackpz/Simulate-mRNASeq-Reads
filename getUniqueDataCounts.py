# A script to take a single column data file of any kind and reduce it to the unique lines
# 2011.11.10
# A. Black P.

# Usage: python getUniqueDataCounts.py input.txt output.txt

import sys

ids = {}

outfile = open(sys.argv[2], 'w')

print 'Loading/counting data\n'

count = 0

for newString in open(sys.argv[1]):
    newString = newString.rstrip()
    if ids.has_key(newString):
        ids[newString] += 1
    else:
        ids[newString] = 1
    count += 1

for key in sorted(ids):
    outfile.write(key + '\t' + str(ids[key]) + '\n')

print count
print 'Finished!'
