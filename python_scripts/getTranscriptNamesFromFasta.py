# A script to take a fasta file of RandomReads.fa and extract the transcript name w/o the carrot
# Original: 2012.05.08
# Original: A. Black P.
# Last: 2012.05.08
# Last: A. Black P.

# Usage: python getTranscriptNamesFromFasta.py input.fa output.txt

import sys

outfile = open(sys.argv[2], 'w')

print 'Loading/counting data\n'

count = 0

for newString in open(sys.argv[1]):
    if '>' in newString:
        newString = newString.rstrip()
        parts = newString.split(' ')
        parts2 = parts[0].split('>')
        outfile.write(str(parts2[1]) + '\n')
        count += 1

print count
print 'Finished!\n'
