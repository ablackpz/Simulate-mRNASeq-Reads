# A script to take ensembl gene ids and get those seqs from a fasta file.
# Original: 2011.11.10
# Original: A. Black P.
# Last modified: 2011.11.10
# Last modified: A. Black P.

# Usage: python extractSeqsFastaById.py input.fasta input.ids output.fasta

import sys, makeRandomTestData

print 'Loading/counting data\n'

count = 0

genes = makeRandomTestData.inputFastaSeq(sys.argv[1])

for newString in open(sys.argv[2], 'r'):
    name = newString.rstrip()
    for key in genes:
        if name in key:
            complete = makeRandomTestData.outputFastaSeq(sys.argv[3], key, genes[key])
    count += 1

print count
print 'Finished!'
