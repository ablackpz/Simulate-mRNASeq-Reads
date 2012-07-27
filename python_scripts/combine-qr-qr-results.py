# A script to take the original fasta and two qr files and combine them so the gene names are preserved and the qr values are merged.
# Original: 2011.10.26
# Original: A. Black P.
# Last: 2011.12.12
# Last: A. Black P.

# Usage: python combine-qr-qr-results.py inputFasta.fasta inputQR1.txt inputQR2.txt output.txt

import sys, makeRandomTestData

outfile = open(sys.argv[4], 'w')

print 'Loading/counting data\n'

count = 0
genes1 = {}
genes2 = {}
genes3 = {}

count = 0
for newString in open(sys.argv[1]):
    if newString[0] == '>':
        parts = newString.split(' ')
        genes1[count] = parts[0]
        count += 1

count = 0
for newString in open(sys.argv[2]):
    genes2[count] = newString.rstrip()
    count += 1

count = 0
for newString in open(sys.argv[3]):
    genes3[count] = newString.rstrip()
    count += 1

for i in range(0, count):
    outfile.write(genes1[i] + '\t' + str(genes2[i]) + '\t' + str(genes3[i]) + '\n')

print count
print 'Finished!'
