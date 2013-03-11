# A script to get rid of junk in bwa sam file
# Created: 2012.10.14
# Creator: A. Black P.
# Modified: 2012.10.14
# Modifier: A. Black P.

# Usage: python getBwaSamParse.py input.2col output.2col

import sys

infile = sys.argv[1]
outfile = open(sys.argv[2], 'w')


for newString in open(infile):
    newString = newString.rstrip()
#    print newString
    parts = newString.split(' ')
    if len(parts) >= 2:
#        print parts[1]
        parts2 = parts[1].split(':')
        parts3 = parts2[2].split(',')
        outfile.write(parts[0] + '\t' + parts3[0] + '\n')

print "Finished!"
