# A script to take output from khmer and bowtie and output a file containing the gene names, median, and read count
# Original: 2011.10.26
# Original: A. Black P.
# Last: 2011.10.26
# Last: A. Black P.

# Usage: python combine-khmer-bowtie-results.py inputKhmer.txt inputBowtie.txt output.txt

import sys, makeRandomTestData

outfile = open(sys.argv[3], 'w')

print 'Loading/counting data\n'

count = 0
genesK = {}
genesB = {}

for newString in open(sys.argv[1]):
    newString = newString.rstrip()
    parts = newString.split(' ')
    parts[0] = parts[0].lstrip('>')
#    print parts
    genesK[parts[0]] = parts[1]
#    print parts[0]

for newString in open(sys.argv[2]):
    newString = newString.rstrip()
    parts = newString.split(' ')
    parts[1] = parts[1].rstrip()
    genesB[parts[0]] = parts[1]
#    print parts[0]

for gene in sorted(genesK.keys()):
    if genesB.has_key(gene):
        outfile.write(gene + '\t' + str(genesK[gene]) + '\t' + str(genesB[gene]) + '\n')
        genesB.pop(gene)
    else:
#        print 'Gene', gene, ' not found'
        outfile.write(gene + '\t' + str(genesK[gene] + '\t' + 'NaN' + '\n'))
    genesK.pop(gene)
    count += 1

for gene in sorted(genesB.keys()):
    outfile.write(gene + '\t' + 'NaN' + '\t' + str(genesB[gene]) + '\n')

print count
print 'Finished!'
