# A script to get the last column of a reads txt file
# 2011.10.20
# A. Black P.

# Usage: python remove-method-readtxt.py input.txt output.txt

import sys

outfile = open(sys.argv[2], 'w')

print 'Loading/counting data\n'

count = 0

for newString in open(sys.argv[1]):
    parts = newString.split('\t')
    outfile.write(parts[-1] + '\n')
    count += 1

print count
print 'Finished!'
