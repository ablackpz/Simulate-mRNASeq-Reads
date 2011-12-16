# A script to initialize a dictionary based on the kmers in the transcriptome and then output kmer counts per gene
# Date Created: 2011.12.08
# Author: A. Black P.

# Usage: python countKmersTranscriptomePerGene.py transcriptome.fa transcriptomeKmerCount.txt geneKmerCount.txt kLength

import makeRandomTestData, os, random, sys


k = int(sys.argv[4])
infileTransName = sys.argv[1]
infileTransKmerName = sys.argv[2]
outfileName = sys.argv[3]
kmers = {}

kmers = makeRandomTestData.inputDictionaryContent(infileTransKmerName, kmers)
fasta = makeRandomTestData.inputFastaSeq(infileTransName)
counter = 0

for entry in fasta:
    print >> sys.stderr, counter
    kmers = makeRandomTestData.zeroInitializedDictionary(kmers)
    kmers = makeRandomTestData.countKmersInitialized(fasta[entry], k, kmers)
    count = makeRandomTestData.outputDictionaryContentNoKey(outfileName, kmers)
    counter += 1

print >> sys.stderr, 'Number of kmers: ', count

print >> sys.stderr, 'Finished!'
