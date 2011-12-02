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
    parts = newString.split('\t')
    parts[0] = parts[0].lstrip('>')
    genesK[parts[0]] = parts[1]
#    print parts[0]

for newString in open(sys.argv[2]):
    newString = newString.rstrip()
    parts = newString.split('\t')
    parts[2] = parts[2].rstrip()
    name = parts[0].split(' ')
    genesB[name[0]] = parts[2]
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
    outfile.write(gene + '\t' + 'NaN' + '\t' + str(genesB[gene]) + '\t')

print count
print 'Finished!'
