# A script to count the number of seqs in a fasta file
# Original: 2011.11.07
# Original: A. Black P.
# Last modified: 2011.11.07
# Last modified: A. Black P.

# Usage: python countFasta.py input.fasta

import sys, makeRandomTestData

print 'Loading/counting data\n'

count = 0

genes = makeRandomTestData.inputFastaSeq(sys.argv[1])
print len(genes)

print 'Finished!'
