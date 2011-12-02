# A script to take the list of incorrectly mapped bowtie reads and squash it down into a list of unique gene ids
# 2011.11.10
# A. Black P.

# Usage: python getUniqueIds.py twoColumnInput.txt output.txt

import sys

ids = {}

outfile = open(sys.argv[2], 'w')

print 'Loading/counting data\n'

count = 0

for newString in open(sys.argv[1]):
    newString = newString.rstrip()
    parts = newString.split(' ')
    if ids.has_key(parts[0]):
        pass
    else:
        ids[parts[0]] = 1
    count += 1
    if ids.has_key(parts[1]):
        pass
    else:
        ids[parts[1]] = 1

for key in sorted(ids):
    outfile.write(key + '\n')

print count
print 'Finished!'
