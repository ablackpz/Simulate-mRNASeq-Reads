# A script to output the lengths of genes in a fasta file
# 2011.10.24
# A. Black P.

# Usage: python count-gene-length.py input.txt output.txt

import sys, makeRandomTestData

outfile = open(sys.argv[2], 'w')

print 'Loading/counting data\n'

count = 0

genes = makeRandomTestData.inputFastaSeq(sys.argv[1])
for gene in genes.keys():
    outfile.write(gene + '\t' + str(len(genes[gene])) + '\n')
    count += 1

print count
print 'Finished!'
