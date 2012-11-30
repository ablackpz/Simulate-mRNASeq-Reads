# A script to take output two bowtie files and a reference transcript name file and output a file containing the transcript names and read counts
# Original: 2011.10.26
# Original: A. Black P.
# Last: 2012.05.08
# Last: A. Black P.

# Usage: python combine-bowtie-bowtie-refFile-results.py refNames.txt inputBowtie1.txt inputBowtie2.txt output.txt

import sys, makeRandomTestData

outfile = open(sys.argv[4], 'w')

print 'Loading/counting data\n'

count = 0
#transcriptNames = {}
transcripts1 = {}
transcripts2 = {}

for newString in open(sys.argv[1]):
    newString = newString.rstrip()
    if '>' in newString:
        parts = newString.split('>')
        newString = parts[1]
        transcripts1[newString] = 'NaN'
        transcripts2[newString] = 'NaN'

for newString in open(sys.argv[2]):
    newString = newString.rstrip()
    parts = newString.split('\t')
    parts[0] = parts[0].lstrip('>')
    if transcripts1.has_key(parts[0]):
        transcripts1[parts[0]] = parts[1]
    else:
        print "New key in file 1 that is not present in ref file"
#    genesK[parts[0]] = parts[1]
#    print parts[0]

for newString in open(sys.argv[3]):
    newString = newString.rstrip()
    parts = newString.split('\t')
    parts[0] = parts[0].lstrip('>')
    if transcripts2.has_key(parts[0]):
        transcripts2[parts[0]] = parts[1]
    else:
        print "New key in file 2 that is not present in ref file"
#    genesB[parts[0]] = parts[1]
#    print parts[0]

for name in transcripts1:
#    print name, transcripts1[name], transcripts2[name]
    outfile.write(name + '\t' + str(transcripts1[name]) + '\t' + str(transcripts2[name]) + '\n')
    count += 1
#for gene in sorted(genesK.keys()):
#    if genesB.has_key(gene):
#        outfile.write(gene + '\t' + str(genesK[gene]) + '\t' + str(genesB[gene]) + '\n')
#        genesB.pop(gene)
#    else:
#        print 'Gene', gene, ' not found'
#        outfile.write(gene + '\t' + str(genesK[gene] + '\t' + 'NaN' + '\n'))
#    genesK.pop(gene)
#    count += 1
#
#for gene in sorted(genesB.keys()):
#    outfile.write(gene + '\t' + 'NaN' + '\t' + str(genesB[gene]) + '\n')

print count
print 'Finished!'
